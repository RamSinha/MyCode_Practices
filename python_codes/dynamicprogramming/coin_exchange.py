#!/usr/bin/python
import sys
import numpy as np

def count_solutions(s,n):
    lookup = [[0 for i in range(n+1)] for _ in range(len(s))]
    for i in range(len(s)):
        lookup[i][0]=1
    for c in range(0,len(s)):
        for v in range(1,n+1):
            included = lookup[c][v-s[c]] if v-s[c] >= 0 else 0
            notincluded = lookup[c-1][v] if c-1 >= 0 else 0
            lookup[c][v] = included + notincluded
    print np.matrix(lookup)
    print 'Total number of available combinations: {}'.format(lookup[len(s)-1][n])

if __name__ == '__main__':
    s=map(lambda x: int(x),raw_input('Enter available coins, ex: 1,2,3\n').split(','))
    n= int(raw_input('Enter the ammount, ex: 4\n'))
    count_solutions(s,n)
