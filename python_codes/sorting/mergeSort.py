#!/usr/bin/python
import sys
def merge(array, p, q, r):
    firstPart = array[p:q+1]
    secondPart = array[q+1:r+1]
    firstPart.append(sys.maxint)
    secondPart.append(sys.maxint)
    i = 0
    j = 0
    for k in range (p,r+1):
        if firstPart[i]<secondPart[j]:
            array[k] = firstPart[i]
            i+=1
        else:
            array[k] = secondPart[j]
            j+=1

def mergeSort(array,p,r):
    if p < r:
        q = ( p + r )/2 
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)
if __name__=='__main__':
    input = [int(i) for i in  raw_input().split(' ')]
    mergeSort(input,0, len(input)-1)
    print input
