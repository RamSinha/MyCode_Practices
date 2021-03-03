#!/usr/bin/python

import numpy as np 
import sys

'''
Formula to generate optimal binary search tree given the probability of access of keys (keys are in sorted order)
e[i,j] = P(r) + e[i, r-1] + w[i,r-1] + e[r+1, i] + w[r+1, i]
=>
e[i,j] = e[i,r-1] + e[r+1,j] + w[i,j]
And 
w[i,j] = w[i,j-1] + p[j] (key-probability) + d[j] (dummy key probability) 
w[i,j] ==> sum of all the probability of the node of sub-tree, if the tree becomes sub-tree of some root (r), then overall tree's cost is increased by w[i,j]

Also:
    e[i][i-1] = d[i-1]  => to address the boundary case when K[i] is picked as root, then by definition
    left sub-tree will be (K[i] <-> K[i-1]) empty hence only dummpy node will be considered i.e d[i-1]
    Same argument will hold for other extreme when K[j] is picked and right sub-tree will be empty.
    e[j+1][j] = d[j]

       1    2    3    4    5    <-- Index to keys in code
  K0   K1   K2   K3   K4   K5   <-- K0 is added just to maintain schemantics,Keys will accessed from 1
    D0   D1   D2   D3   D4   D5  
'''

def generateOptimumTree(k,d,keys):
    n = len(k) #total number of keys
    w = [[0] * n for _ in range(n+1)]
    root = [[None] * n for _ in range(n+1)]
    e = [[None] * n for _ in range(n+1)]
    for i in range(1, n+1):
        e[i][i-1] = d[i-1]
        w[i][i-1] = d[i-1]
    for l in range(0,len(k)):
        for i in range(1, len(k)-l):
            j=i+l
            w[i][j] = w[i][j-1] + k[j] + d[j]
            e[i][j] = sys.maxint
            for r in range(i,j+1):
                c= e[i][r-1] + e[r+1][j] + w[i][j]
                if c < e[i][j]:
                    e[i][j] = c
                    root[i][j] = r
    return (w,root,e)

def generateOptimumTreeWithoutPositionalHack(keyPriority, d):
    n = len(keyPriority) #total number of keys
    w = [[0] * len(d) for _ in range(n + 2)]
    root = [[None] * len(d) for _ in range(n+2)]
    e = [[None] * len(d) for _ in range(n+2)]
    for i in range(1, n+2):
        e[i][i-1] = d[i-1]
        w[i][i-1] = d[i-1]
    for l in range(1,n+1):
        for i in range(1, n-l + 2):
            j=i+l-1
            w[i][j] = w[i][j-1] + keyPriority[j-1] + d[j]
            e[i][j] = sys.maxint
            for r in range(i,j+1):
                c= e[i][r-1] + e[r+1][j] + w[i][j]
                if c < e[i][j]:
                    e[i][j] = c
                    root[i][j] = r
    print 'weight: \n{w}'.format(w=np.matrix(w))
    print 'root: \n{r}'.format(r=np.matrix(root))
    print 'cost: \n{c}'.format(c=np.matrix(e))
    printOptimalBinarySearchTree(root, 1, n, 0)

def printOptimalBinarySearchTree(root, i, j, last):
    if i == j:
        if last > root[i][j]:
            print 'k{} is {} child of k{}'.format(root[i][j], 'left', last)
        else:
            print 'k{} is {} child of k{}'.format(root[i][j], 'right', last)
        printOptimalBinarySearchTree(root, i, i-1, i)    
        printOptimalBinarySearchTree(root, j+1, j, j)    
        return    
    if i > j:
        if i == last:
            print 'd{} is {} child of k{}'.format(j, 'left', last)
        else:
            print 'd{} is {} child of k{}'.format(j, 'right', last)
        return    
    r = root[i][j]
    if last == 0:
        print 'k{} is {} of optimal tree'.format(r, 'root')
    elif r > last:
        print 'k{} is {} child of k{}'.format(r, 'right', last)
    else:    
        print 'k{} is {} child of k{}'.format(r, 'left', last)
    printOptimalBinarySearchTree(root, i, r-1, r)    
    printOptimalBinarySearchTree(root, r+1, j, r)    

            
        

if __name__ == '__main__':
    keyPriority = [0.15, 0.10, 0.05, 0.10, 0.20] # Added zero at the start to keep then structural schemantics of the algorithm.
    keyPriorityPadded = [0, 0.15, 0.10, 0.05, 0.10, 0.20] # Added zero at the start to keep then structural schemantics of the algorithm.
    dummyNodePriority = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    keys = map(lambda x: 'key{x}'.format(x = x), range(1,len(keyPriorityPadded)))
    (weight,root,cost) = generateOptimumTree(keyPriorityPadded, dummyNodePriority, keys)
    print 'weight: \n{w}'.format(w=np.matrix(weight[1:]))
    print 'root: \n{r}'.format(r=np.matrix(root[1:]))
    print 'cost: \n{c}'.format(c=np.matrix(cost[1:]))
    print ("\n ***************\n")
    generateOptimumTreeWithoutPositionalHack(keyPriority, dummyNodePriority)
