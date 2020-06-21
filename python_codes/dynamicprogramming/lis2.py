#!/usr/bin/python
import numpy as np
import copy 
from operator import itemgetter

def lis(a):
    indexArray = range(0,len(a))
    result = [0]
    if not a:
        return 0
    r = [None]*len(a)
    r[0]=a[0]
    result[0]=a[0]
    l = 1
    for i in range(1, len(a)):
        if a[i] < r[0]:
            r[0] = a[i]
        elif a[i] > r[l-1]:
            r[l]=a[i]
            result = copy.copy(r)
            l+=1
        else:    
            k = findIndex(r,a[i],-1,l-1)
            r[k]=a[i]
    return result

def findIndex(s,pivot,start,end):
    '''
    Modified binary search to return index for mininum value greater than pivot
    for the first time start shall be -1
    '''
    while end - start > 1:  
        mid = end + (start - end) / 2 
        if s[mid] >= pivot:
            end = mid
        else:
            start = mid
    #print "s={s}, pivot={pivot},start={start},end={end}".format(s=s,pivot=pivot,start=start,end=end)        
    return end        

def printSolutionUtil(sol,seq,index):
    if index >=0:
        printSolutionUtil(sol, seq, sol[index])
        print seq[index],
    
def doTest(seq):
    result = lis(seq)
    r = [i for i in result if i!= None]
    print "length of lis: {result}".format(result=len(r))
    #index, value = max(enumerate(sol), key=itemgetter(1))
    #printSolutionUtil(sol,seq,index)

if __name__ == '__main__':
    seq=map(lambda x : int(x), raw_input("enter seq of integer, ex: 0,8,4,12,2,10,6,14,1,9,5,13\n").split(","))
    doTest(seq)
