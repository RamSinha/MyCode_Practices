#!/usr/bin/python

import subprocess
import sys
import string
import exceptions

import guavus.glogging.glogger as glogger

class HdfsException(Exception):
    class ErrorCodes:
        FILE_NOT_FOUND_ERROR = 501
        NAME_NODE_IN_SAFE_MODE_ERROR = 502
        CONNECTION_ERROR = 503
        FILE_ALREADY_EXISTS_ERROR = 504
        DATA_NODE_DOWN_ERROR = 505
        OVERWRITE_NON_DIRECTORY_ERROR = 506
        DIRECTORY_NOT_FOUND = 507
        UNKNOWN_ERROR = 508

    def __init__(self, errNo, errMsg):
        self.errNo = errNo
        self.errMsg = errMsg

    def __str__(self):
        return "Error-" + str(self.errNo) + ": " + self.errMsg

class HdfsFileNotFoundException(HdfsException):
    def __init__(self, errMsg = 'file not found'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.FILE_NOT_FOUND_ERROR, errMsg)

class HdfsNameNodeInSafeModeException(HdfsException):
    def __init__(self, errMsg = 'name node is in safe mode'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.NAME_NODE_IN_SAFE_MODE_ERROR, errMsg)

class HdfsConnectionException(HdfsException):
    def __init__(self, errMsg = 'connection error'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.CONNECTION_ERROR, errMsg)

class HdfsFileAlreadyExistsException(HdfsException):
    def __init__(self, errMsg = 'file already exists'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.FILE_ALREADY_EXISTS_ERROR, errMsg)

class HdfsDataNodeDownException(HdfsException):
    def __init__(self, errMsg = 'data node is down'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.DATA_NODE_DOWN_ERROR, errMsg)

class HdfsOverwriteNonDirectoryException(HdfsException):
    def __init__(self, errMsg = 'can not overwrite non directory'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.OVERWRITE_NON_DIRECTORY_ERROR, errMsg)

class HdfsDirectoryNotFoundException(HdfsException):
    def __init__(self, errMsg = 'directory not found'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.DIRECTORY_NOT_FOUND, errMsg)

class HdfsUnknownException(HdfsException):
    def __init__(self, errMsg = 'unknown error'):
        HdfsException.__init__(self, HdfsException.ErrorCodes.UNKNOWN_ERROR, errMsg)


class HdfsCommandExecutor(object):
    CONNECTION_FAILED_STR = 'failed on connection exception'
    FILE_NOT_FOUND_STR = 'no such file or directory'
    FILE_NOT_EXIST_STR = 'file does not exist'
    NAME_NODE_SAFE_MODE_STR = 'name node is in safe mode'
    FILE_ALREADY_EXIST_STR = 'already exists'
    DATA_NODE_DOWN_WRITE_STR = 'exception closing file'
    DATA_NODE_DOWN_READ_STR = 'could not obtain block'
    FAILED_TO_RENAME_STR = 'failed to rename'
    CAN_NOT_OVERWRITE_NON_DIR_STR = 'cannot overwrite non directory'
    DESTINATION_SHOULD_BE_DIR_STR = 'should be a directory'
    UNKNOWN_ERROR_STR = 'unknown error'

    def __init__(self, hadoopCmdPath = "/opt/hadoop/bin/hadoop"):
        self.hadoopCmd = hadoopCmdPath

    # Executes command silently. All exceptions occurred in this method are ignored.
    def executeSilently(self, command, *commandArgs):
        try:
            self.execute(command, *commandArgs)
        except:
            pass
        return 0
        
    # Executes command.
    def execute(self, command, *commandArgs):
        commandWithOptionList = command.split()
        commandName = commandWithOptionList[0]
        commandOptions = ''
        if len(commandWithOptionList) > 1:
            for option in commandWithOptionList[1::]:
                commandOptions = commandOptions + " " + option
        args = ''
        for arg in commandArgs:
            args = args + " " + arg
        if commandWithOptionList[0].startswith("rm"):
             return self.__rm(commandOptions, args)
        elif commandWithOptionList[0].startswith("test"):
            return self.__test(commandOptions, args)
        elif commandWithOptionList[0].startswith("put"):
            return self.__put(commandOptions, args)
        elif commandWithOptionList[0].startswith("cat"):
            return self.__cat(commandOptions, args)
        elif commandWithOptionList[0].startswith("mv"):
            return self.__mv(commandOptions, args)
        elif commandWithOptionList[0].startswith("ls"):
            return self.__ls(commandOptions, args)
        else:
            glogger.warn('command not supported')
            return -1


    def __rm(self, commandOptions, args):
        command = self.hadoopCmd + " fs -rm " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        if process.returncode != 0:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not remove file(s) [" + args + " ]\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)
        else:
            glogger.debug("removed file(s) [" + args + " ] successfully")
            return 0


    def __test(self, commandOptions, args):
        command = self.hadoopCmd + " fs -test " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        if process.returncode == 0:
            glogger.debug(command + ": 0")
            return 0
        elif process.returncode == 1:
            glogger.debug(command + ": 1")
            return 1
        else:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not execute test on file [" + args + " ]\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)


    def __ls(self, commandOptions, args):
        command = self.hadoopCmd + " fs -ls " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        if process.returncode != 0:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not ls file(s) [" + args + " ]\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)
        else:
            glogger.debug("ls file(s) [" + args + " ] result:\n" + ret[0])
            return ret[0]


    def __put(self, commandOptions, args):
        command = self.hadoopCmd + " fs -put " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        files = args.split()
        srcFiles = files[0:len(files) - 1]
        destFile = files[len(files) - 1]
        inputFiles = ''
        for file in srcFiles:
            inputFiles = inputFiles + ' ' + file
        if process.returncode != 0:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not put file(s) [" + inputFiles + " ] at " + destFile + "\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)
        else:
            glogger.debug("put file(s) [" + inputFiles + " ] at " + destFile +" successfully")
            return 0


    def __mv(self, commandOptions, args):
        command = self.hadoopCmd + " fs -mv " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        files = args.split()
        srcFiles = files[0:len(files) - 1]
        destFile = files[len(files) - 1]
        inputFiles = ''
        for file in srcFiles:
            inputFiles = inputFiles + ' ' + file
        if process.returncode != 0:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not move file(s)/directory [" + inputFiles + " ] to " + destFile + "\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)
        else:
            glogger.debug("moved file(s) [" + inputFiles + " ] at " + destFile +" successfully")
            return 0


    def __cat(self, commandOptions, args):
        command = self.hadoopCmd + " fs -cat " + commandOptions + " " + args
        glogger.debug("executing command = " + command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        if process.returncode != 0:
            errorString = self.__getErrorStringFromLog(ret[1])
            exceptionMessage = "could not cat file(s) [" + args + " ]\nFailure Reason: " + errorString + ' (Hdfs Command Return Code: ' + str(process.returncode) + ')\n' + ret[1]
            raise self.__getExceptionFromErrorString(errorString, exceptionMessage)
        else:
            glogger.debug("cat file(s) [" + args + " ] result:\n" + ret[0])
            return ret[0]
    
    def __getErrorStringFromLog(self, errorLogs):
        errMsgs = errorLogs.rstrip().splitlines()
        for line in errMsgs:
            lowerCaseLine = line.lower()
            if lowerCaseLine.find(HdfsCommandExecutor.CONNECTION_FAILED_STR) != -1:
                return HdfsCommandExecutor.CONNECTION_FAILED_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.FILE_NOT_FOUND_STR) != -1:
                return HdfsCommandExecutor.FILE_NOT_FOUND_STR 
            elif lowerCaseLine.find(HdfsCommandExecutor.FILE_NOT_EXIST_STR) != -1:
                return HdfsCommandExecutor.FILE_NOT_EXIST_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.NAME_NODE_SAFE_MODE_STR) != -1:
                return HdfsCommandExecutor.NAME_NODE_SAFE_MODE_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.FILE_ALREADY_EXIST_STR) != -1:
                return HdfsCommandExecutor.FILE_ALREADY_EXIST_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.DATA_NODE_DOWN_WRITE_STR) != -1:
                return HdfsCommandExecutor.DATA_NODE_DOWN_WRITE_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.DATA_NODE_DOWN_READ_STR) != -1:
                return HdfsCommandExecutor.DATA_NODE_DOWN_READ_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.FAILED_TO_RENAME_STR) != -1:
                return HdfsCommandExecutor.FAILED_TO_RENAME_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.CAN_NOT_OVERWRITE_NON_DIR_STR) != -1:
                return HdfsCommandExecutor.CAN_NOT_OVERWRITE_NON_DIR_STR
            elif lowerCaseLine.find(HdfsCommandExecutor.DESTINATION_SHOULD_BE_DIR_STR) != -1:
                return HdfsCommandExecutor.DESTINATION_SHOULD_BE_DIR_STR
        return HdfsCommandExecutor.UNKNOWN_ERROR_STR
    
    def __getExceptionFromErrorString(self, errorString, exceptionMessage):
            if errorString == HdfsCommandExecutor.CONNECTION_FAILED_STR:
                return HdfsConnectionException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.FILE_NOT_FOUND_STR:
                return HdfsFileNotFoundException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.FILE_NOT_EXIST_STR:
                return HdfsFileNotFoundException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.NAME_NODE_SAFE_MODE_STR:
                return HdfsNameNodeInSafeModeException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.FILE_ALREADY_EXIST_STR:
                return HdfsFileAlreadyExistsException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.DATA_NODE_DOWN_WRITE_STR:
                return HdfsDataNodeDownException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.DATA_NODE_DOWN_READ_STR:
                return HdfsDataNodeDownException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.FAILED_TO_RENAME_STR:
                return HdfsFileAlreadyExistsException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.CAN_NOT_OVERWRITE_NON_DIR_STR:
                return HdfsOverwriteNonDirectoryException(exceptionMessage)
            elif errorString == HdfsCommandExecutor.DESTINATION_SHOULD_BE_DIR_STR:
                return HdfsDirectoryNotFoundException(exceptionMessage)
            else:
                return HdfsUnknownException(exceptionMessage)
        

hdfsCommandExecutor = HdfsCommandExecutor()
          