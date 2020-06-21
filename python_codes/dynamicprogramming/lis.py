#!/usr/bin/python
import numpy as np
import copy 
from operator import itemgetter
def lis(a):
    result = [1]*len(seq)
    sol = [None]*len(seq)
    for i in range(0,len(seq)):
        for j in range(0,i+1):
            if a[i] > a[j]:
                if result[j] + 1 > result[i]:
                    result[i] = 1 + result[j]
                    sol[i]=[i, j, result[i]] #apply lookup on sol to contruct the solution
    print result
    return result

def findLargestIndex(seq):
    maxLength = -1
    indexOfLargest = -1
    for i in range(len(seq)):
        k,v = seq[i]
        if k > maxLength:
            indexOfLargest = i
            maxLength=k
    return indexOfLargest

if __name__ == '__main__':
    seq=map(lambda x : int(x), raw_input("enter seq of integer: ").split(","))
    print "length of lis is: {result}".format(result=max(lis(seq)))
    #result.sort(key=itemgetter(0), reverse=True)
    #prev = None
    #largestIndex = findLargestIndex(result)
    #scope = len(result)
    #while True:
    #    i = findLargestIndex(result[0:scope])
    #    if i >= 0:
    #        solution.append(seq[i])
    #        scope=i
    #    else:
    #        break
    #solution.reverse()
    #print solution
