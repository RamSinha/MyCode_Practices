#!/usr/bin/python
import numpy as nm
def isInterWeavingString(one, two, three):
    if len(one) + len(two) != len(three):
        return False
    a = [[None for _ in range(len(one) + 1 )] for _ in range(len(two) + 1)]
    a[0][0] = True
    for j in range(1, len(one) + 1):
        a[0][j] = a[0][j-1] and one[j-1] == three[j-1]
            
    for i in range(1, len(two) + 1):
        a[i][0] = a[i-1][0] and two[i-1] == three[i-1]

    for i in range(1,len(two) + 1 ):
        for j in range (1, len (one) + 1 ):
            k = i + j 
            if k <= len(three):
                #print (one[j-1], three[k-1])
                a[i][j] = a[i][j-1] and one[j-1] == three[k-1]
                if not a[i][j]:
                    print (two[i-1] ,  three[k-1])
                    a[i][j] = a[i-1][j] and two[i-1] == three[k-1]
    print(nm.matrix(a))
            

isInterWeavingString('algoexpert', 'your-dream-job', 'your-algodream-expertjob')
