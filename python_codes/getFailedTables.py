#!/usr/bin/python
import os
import subprocess
import sys


def run_command_silently(command):
    status =os.system(command)
    return (status >> 8)

if __name__ == '__main__':
     print (sys.argv)
     assert len(sys.argv) > 1
     logFile = sys.argv[1]
     getLaunchedFileCommand = """grep "Start SparkSQL ETL for hiveTableName" """ + logFile + """ | awk -F "Start SparkSQL ETL for hiveTableName=" '{ print $2 }' | awk -F "," '{ print $1 }' > total_launched""" 
     getCompletedFileCommand = """grep "End SparkSQL ETL for hiveTableName=" """ + logFile + """ | awk -F "End SparkSQL ETL for hiveTableName=" '{ print $2 }' | awk -F "," '{ print $1 }' > total_completed"""
     run_command_silently(getLaunchedFileCommand)
     run_command_silently(getCompletedFileCommand)
     pipe = subprocess.Popen('grep -F -x -v -f total_completed total_launched', stdout=subprocess.PIPE, shell=True)
     output = map(lambda x: x.replace("]", ""), map(lambda x: x.replace("[", ""), pipe.communicate()[0].split("\n")))
     status = pipe.poll()
     tablesToRestartFor = [table for table in output if table]
     os.remove(total_launched)
     os.remove(total_completed)
     print ",".join(tablesToRestartFor)
