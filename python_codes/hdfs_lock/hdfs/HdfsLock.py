#!/usr/bin/python

import subprocess
import re
import os
import socket
import sys
import shutil
import shlex
import time
import string
import datetime
import types
import exceptions
import math

import ooziecore.utils.utilities as utilities

from ooziecore.lib.hdfs.HdfsCommandExecutor import hdfsCommandExecutor, HdfsException, HdfsFileNotFoundException, HdfsDataNodeDownException

import guavus.glogging.glogger as glogger


class HdfsLockException(HdfsException):
    class ErrorCodes:
        NO_LOCK_FOUND_ERROR = 601
        LOCK_RELEASE_ERROR = 602
        LOCK_TIMEOUT_ERROR = 603
        INTERNAL_ERROR = 604
        
    def __init__(self, errNo, errMsg):
        HdfsException.__init__(self, errNo, errMsg)

class HdfsNoLockFoundException(HdfsLockException):
    def __init__(self, errMsg = 'no lock found for client'):
        HdfsLockException.__init__(self, HdfsLockException.ErrorCodes.NO_LOCK_FOUND_ERROR, errMsg)
   
class HdfsLockReleaseException(HdfsLockException):
    def __init__(self, errMsg = 'failed to release the lock'):
        HdfsLockException.__init__(self, HdfsLockException.ErrorCodes.LOCK_RELEASE_ERROR, errMsg)

class HdfsLockTimeoutException(HdfsLockException):
    def __init__(self, errMsg = 'failed to acquire lock in specified time'):
        HdfsLockException.__init__(self, HdfsLockException.ErrorCodes.LOCK_TIMEOUT_ERROR, errMsg)

class HdfsLockInternalException(HdfsLockException):
    def __init__(self, errMsg = 'internal error occurred'):
        HdfsLockException.__init__(self, HdfsLockException.ErrorCodes.INTERNAL_ERROR, errMsg)



class HdfsLock:    
    tmpDirectory = '/tmp'
    lockBaseDirectory = '/data'
    '''
    lockFileName: name of the lock file. It will be created inside /data
    lockExpiryPeriod: lock expire time in seconds
    '''
    def __init__(self, lockFileName, lockExpiryPeriod = 30):
        if not isinstance(lockFileName, str) or lockFileName == "":
            raise ValueError("lock file name is string type and can not be empty.")
        if not isinstance(lockExpiryPeriod, int) or lockExpiryPeriod <= 0:
            raise ValueError("lock expiry period is int type and can not be <= 0.")
        clientIP = socket.gethostbyname(socket.gethostname())
        if not clientIP or clientIP == '0.0.0.0' or clientIP == '127.0.0.1':
            raise Exception("could not retrieve ip address of client")
        ipTokens = clientIP.split('.')
        if len(ipTokens) != 4 or ipTokens[0] == '127':
            raise Exception("could not retrieve ip address of client")

        self.lockname = lockFileName
        self.lockExpiryPeriod = lockExpiryPeriod
        self.lockBaseDir = HdfsLock.lockBaseDirectory
        self.tmpDir = HdfsLock.tmpDirectory
        self.clientIP = clientIP
        self.pid = str(os.getpid())
        self.clientId = self.clientIP + "," + self.pid 
        glogger.debug(str(self))

    ''' 
    throws HdfsLockError.LOCK_TIMEOUT_ERROR if lock is non blocking and HdfsLockError.LOCK_INTERNAL_ERROR
    '''
    def acquire(self, waitPeriod = 0):
        if not isinstance(waitPeriod, int) or waitPeriod < 0:
            raise ValueError("wait period is integer type and can not be < 0.")
        blockingLock = True
        if waitPeriod != 0:
            blockingLock = False
        glogger.debug(self.clientId + " acquiring lock...")
        start = time.time()
        if self.__hasAlreadyAcquiredLock():
            glogger.debug(self.clientId + " has already acquired lock successfully")
            return True
        if (self.__isLockFree() and self.__createLockFile() == 0):
            glogger.debug(self.clientId + " has acquired lock successfully")
            return True
        end = time.time()
        delay = int(end - start)
        waitPeriod -= delay
        lockAquired = False
        if blockingLock or waitPeriod > 0:
            lockAquired = self.__acquireLockInternal(blockingLock, waitPeriod)

        if lockAquired:
            glogger.debug(self.clientId + " has acquired lock successfully")
        elif not blockingLock:         
            glogger.debug(self.clientId + " could not acquire lock in specified time")
        return lockAquired

    ''' 
    throws HdfsLockError.NO_LOCK_EXIST_ERROR, HdfsLockError.LOCK_RELEASE_ERROR
    '''
    def release(self):
        glogger.debug(self.clientId + " releasing lock...")
        if self.__removeLockFile():
            glogger.debug(self.clientId + " has released lock successfully")


    ''' 
    throws HdfsLockError.LOCK_RELEASE_ERROR
    '''
    @staticmethod
    def releaseForcefully(lockFileName):
        lockFilePath = HdfsLock.lockBaseDirectory + '/' + lockFileName
        glogger.debug("trying to release lock " + lockFilePath + " forcefully")
        try:
            status = hdfsCommandExecutor.execute('rm', lockFilePath)
            if status == 0:
                glogger.debug("released lock " + lockFilePath + " successfully")
        except HdfsFileNotFoundException:
            glogger.debug("No lock found with name = " + lockFilePath)
        except HdfsException as ex:
            errorMessage = "could not release lock = " + lockFilePath + "\n" + str(ex) + "\n"
            raise HdfsLockReleaseException(errorMessage)

    def __acquireLockInternal(self, blockingLock, timeout):
        waitPeriod = 3
        if not blockingLock:
            waitPeriod = min(3, timeout)
        utilities.runCommandSilently('sleep ' + str(waitPeriod))
        elapsedTime = waitPeriod
        glogger.debug(self.clientId + " trying again to acquire lock")
        start = time.time()
        if not self.__isLockFree():
            if blockingLock:
                self.__waitForLockInfinitely()
            else:
                end = time.time()
                delay = int(end-start)
                remainingTime = timeout - elapsedTime - delay
                if remainingTime <= 0:
                    return False
                timeExpired,elapsedTimeInWait = self.__timedWaitForLock(remainingTime)
                if timeExpired:
                    return False
                elapsedTime += elapsedTimeInWait
                start = time.time()

        if self.__createLockFile() != 0:
            end = time.time()
            delay = int(end-start)
            remainingTime = timeout - elapsedTime - delay
            if not blockingLock and remainingTime <= 0:
                return False
            return self.__acquireLockInternal(blockingLock, remainingTime)
        return True


    def __waitForLockInfinitely(self):
        glogger.debug(self.clientId + " started waiting infinitely for lock to be free")
        waitPeriod = 3
        done = False
        while not done:
            utilities.runCommand("sleep " + str(waitPeriod))
            glogger.debug("lock is not free trying again for " + self.clientId)
            done = self.__isLockFree()
        glogger.debug(self.clientId + " found the lock free")
        return 0


    def __timedWaitForLock(self, timeout):
        glogger.debug(self.clientId + " started waiting for " + str(timeout) + " seconds for lock to be free")
        elapsedWaitingTime = 0
        done = False
        timeExpired = False
        while not done:
            waitPeriod = min(3, timeout - elapsedWaitingTime)
            if waitPeriod <= 0:
                waitPeriod = 0
            utilities.runCommand("sleep " + str(waitPeriod))
            elapsedWaitingTime = elapsedWaitingTime + waitPeriod
            if elapsedWaitingTime >= timeout:
                timeExpired = True
                done = True
            else:
                glogger.debug("lock is not free. " + self.clientId + " trying again")
                start = time.time()
                done = self.__isLockFree()
                end = time.time()
                delay = int(end-start)
                elapsedWaitingTime += delay
        if not timeExpired:
            glogger.debug(self.clientId + " found the lock free after waiting for " + str(elapsedWaitingTime) + " seconds")
        return timeExpired,elapsedWaitingTime


    def __isLockFree(self):
        try:
            status = hdfsCommandExecutor.execute('test -e', self.lockBaseDir + "/" + self.lockname)
            if status == 0:
                lockFileData = hdfsCommandExecutor.execute('cat', self.lockBaseDir + "/" + self.lockname)
                lsResult = hdfsCommandExecutor.execute('ls', self.lockBaseDir + "/" + self.lockname)
                if not self.__isValidLockFile(lockFileData) or not self.__lockingProcessExists(lockFileData) or self.__isLockExpired(lsResult):
                    try:
                        HdfsLock.releaseForcefully(self.lockname)
                        return True
                    except HdfsException, e:
                        glogger.warn(self.clientId + ' could not clear old lock')
                        return False
            elif status == 1:
                glogger.debug(self.clientId + " found lock free")
                return True 
        except HdfsException, ex:
            glogger.warn(self.clientId + " could not check for lock to be free\n" + str(ex) + "\n")
            return False


    def __isValidLockFile(self, lockFileData):
        msgs = lockFileData.rstrip().splitlines()
        if len(msgs) != 1:
            glogger.debug('found invalid lock file')
            return False
        tokens = msgs[0].split(',')
        if len(tokens) != 2:
            glogger.debug('found invalid lock file')
            return False
        return True
        

    def __lockingProcessExists(self, lockFileData):
        msgs = lockFileData.rstrip().splitlines()
        tokens = msgs[0].split(',')
        user = 'root'
        ip = tokens[0]
        pid = tokens[1]
        processExists = False
        if self.clientIP == ip:
            try:
                os.kill(int(pid), 0)
                processExists = True
            except OSError:
                glogger.debug('Locking process(' + pid + ') does not exist on ip ' + ip)
        else:
            retryCount = 3
            while retryCount > 0:
                ssh_opts = "-o ConnectTimeout=5 -o PreferredAuthentications=publickey -o PasswordAuthentication=no -o HostbasedAuthentication=no -o KbdInteractiveAuthentication=no -o GSSAPIAuthentication=no"
                command = "ssh " + ssh_opts + " " + user + "@" + ip + " \"/usr/bin/python -c \\\"exec(\\\\\\\"import os\\\\\\\\nval=0\\\\\\\\ntry:\\\\\\\\n os.kill(" + pid + ",0)\\\\\\\\nexcept OSError:\\\\\\\\n val=1\\\\\\\\nprint val\\\\\\\")\\\"\""
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                ret = process.communicate()
                status = process.returncode
                if status == 0:
                    if ret[0].rstrip() == '0':
                        processExists = True
                    else:
                        glogger.debug('Locking process(' + pid + ') does not exist on remote ip ' + ip)
                    break
                else:
                    retryCount -= 1;
            if retryCount == 0:
                glogger.debug('Retry limit reached. Assuming locking process(' + pid + ') does not exist on remote ip ' + ip)
        return processExists

    def __isLockExpired(self, lsResult):
        lines = lsResult.rstrip().splitlines()
        if len(lines) == 2 and re.search('found', lines[0].lower()):
            tokens = lines[1].split()
            dateStr = tokens[5] + ' ' + tokens[6]
            struct_time = time.strptime(dateStr, '%Y-%m-%d %H:%M')
            hdfsTime = time.mktime(struct_time)
            currentTime = time.time()
            if currentTime - hdfsTime > self.lockExpiryPeriod:
                glogger.debug('lock is expired')
                return True
        return False

    def __createLockFile(self):
        tmpFolder = self.tmpDir + "/" + self.clientId
        command = 'mkdir -p ' + tmpFolder
        status = utilities.runCommandSilently(command)
        if status != 0:
            glogger.warn(self.clientId + " could not create directory " + tmpFolder)
            return -1
        tmpLockFile = tmpFolder + "/" + self.lockname
        command = 'touch ' + tmpLockFile + ' | echo "' + self.clientId + '" > ' + tmpLockFile
        status = utilities.runCommandSilently(command)
        if status != 0:
            glogger.warn(self.clientId + " could not create file " + tmpLockFile)
            command = "rm -rf " + tmpFolder
            utilities.runCommandSilently(command)
            return -1
        try:
            status = hdfsCommandExecutor.execute('put', tmpLockFile, self.lockBaseDir)
            if status == 0:
                glogger.debug(self.clientId + " has created lock file successfully")
        except HdfsDataNodeDownException as ex:
            status = -1
            glogger.warn(self.clientId + " could not create lock file\n" + str(ex) + "\n")
            try:
                glogger.debug(self.clientId + " removing partial lock file")
                HdfsLock.releaseForcefully(self.lockname)
                glogger.debug(self.clientId + " removed partial lock file")
            except HdfsException as e:
                glogger.warn(self.clientId + " could not remove partial lock file\n" + str(e) + "\n")           
        except HdfsException as e:
            status = -1
            glogger.warn(self.clientId + " could not create lock file\n" + str(e) + "\n")
        command = "rm -rf " + tmpFolder
        utilities.runCommandSilently(command)
        return status


    def __hasAlreadyAcquiredLock(self):
        try:
            status = hdfsCommandExecutor.execute('test -e', self.lockBaseDir + "/" + self.lockname)
            if status == 0:
                lockFileData = hdfsCommandExecutor.execute('cat', self.lockBaseDir + "/" + self.lockname)
                lsResult = hdfsCommandExecutor.execute('ls', self.lockBaseDir + "/" + self.lockname)
                if not self.__isValidLockFile(lockFileData) or not self.__lockingProcessExists(lockFileData) or self.__isLockExpired(lsResult):
                    try:
                        HdfsLock.releaseForcefully(self.lockname)
                    except HdfsException, e:
                        glogger.warn(self.clientId + ' could not clear old lock')
                else:
                    msgs = lockFileData.rstrip().splitlines()
                    if msgs[0] == self.clientId:
                        return True
        except HdfsFileNotFoundException:
            pass
        except HdfsException as ex:
            errorMessage = self.clientId + " could not check for already lock acquired\n" + str(ex) + "\n"
            raise HdfsLockInternalException(errorMessage)
        return False

 
    def __removeLockFile(self):
        rVal = ''
        try:
            rVal = hdfsCommandExecutor.execute('cat', self.lockBaseDir + "/" + self.lockname)
        except HdfsException as ex:
            errorMessage = self.clientId + " failed to release lock\n" + str(ex) + "\n"
            raise HdfsLockReleaseException(errorMessage)
        msgs = rVal.rstrip().splitlines()
        if len(msgs) == 1 and msgs[0] == self.clientId:
            retryCount = 0
            count = 3; # max try
            while retryCount < count:
                try:
                    glogger.debug(self.clientId + " trying to remove lock file")
                    status = hdfsCommandExecutor.execute('rm', self.lockBaseDir + "/" + self.lockname)
                    if status == 0:
                        return True
                except HdfsException as ex:
                    glogger.warn(self.clientId + " could not remove lock file\n" + str(ex) + "\n")
                    retryCount = retryCount + 1
            errorMessage = self.clientId + " failed to release lock after trying " + str(count) + " times\n"
            raise HdfsLockReleaseException(errorMessage)
        else:
            glogger.debug(self.clientId + " found lock file data: " + str(msgs))
            errorMessage = "no lock file found for " + self.clientId + "\n"
            raise HdfsNoLockFoundException(errorMessage)

    
    def __str__(self):
        return "id = " + self.clientId +", lock file name = " + self.lockname + ", lock expire period = " + str(self.lockExpiryPeriod)
