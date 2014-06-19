#!/usr/bin/python
import os
import time
import errno
import sys
import glob
sys.path.append('/opt/etc/oozie/common/')
import misc
__author__ = 'vineet.mittal'
class LockUnix:
    lockCheckSleepTimeSec = 10
    lockTimeOutSec = 3600
    fd = None
    lockfile = '/data/ib/setupLock/file.lck'
    openfile = '/data/ib/setupLock/file.opn'
    pid = -1
    def __init__(self, openfile, lockFile, lockTimeOutSec):
        self.openfile = openfile
        self.lockfile = lockFile
        self.lockTimeOutSec = lockTimeOutSec
        self.pid = os.getpid()
        dir = os.path.dirname(openfile)
        if not os.path.exists(dir):
            os.makedirs(dir)
            open(openfile,'w').close()

    def unlockForPID(self, pid):
        lockF = self.lockfile + '.' + str(pid)
        try:
            os.rename(lockF, self.openfile)
            misc.log("Released lock from file " + lockF)
        except OSError as ex:
            if ex.errno == errno.ENOENT:
                misc.log("Lock already released from file " + lockF)

    def getPID(self, fileName):
        return str.replace(fileName,self.lockfile+'.' , '')

    def unlockForFile(self, fileName):
        pid = self.getPID(fileName)
        self.unlockForPID(pid)

    def unlock(self):
        self.unlockForPID(self.pid)

    def takeFileLock(self):
        os.rename(self.openfile, self.lockfile + '.' + str(self.pid))
        misc.log("Locked file " + self.lockfile + '.' + str(self.pid))
    
    def findLockFile(self):
        lockFile = None
        files = glob.glob(self.lockfile + '.*')
        
        if files:
           lockFile = files[0]
        return lockFile
        
    def getLockChangeTime(self):
        file = self.findLockFile()
        if(file):
            try:
                return os.path.getctime(file)
            except Exception:
                pass
        return time.time()

    def isProcessAlive(self, lockfile):
        return os.path.exists("/proc/" + str(self.getPID(lockfile)))

    def lock(self):
        while (True):
            try:
                self.takeFileLock()
                break
            except OSError as ex:
                if ex.errno != errno.ENOENT:
                    misc.log('Got error ' , ex, ' , Continuing without taking any action')
                misc.log ('Going to wait for lock for : ', self.lockCheckSleepTimeSec, ' Seconds')
                time.sleep(self.lockCheckSleepTimeSec)
                lockfile = self.findLockFile()
                isProcessAlive = 1
                if(lockfile):
                   isProcessAlive = self.isProcessAlive(lockfile)
                   if(not isProcessAlive):
                      misc.log("Going to release the lock forcefully as process not Alive")
                      self.unlockForFile(lockfile)
                   if(time.time() - self.getLockChangeTime() >= self.lockTimeOutSec):
                      misc.log("Going to release the lock forcefully as process Took long time to release lock")
                      self.unlockForFile(lockfile)

