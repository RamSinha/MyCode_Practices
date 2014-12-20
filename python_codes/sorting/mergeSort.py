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

l = [1,24,46, 2,3,4,3,56,7,8,9,99,777,34232]
#merge(l,0,2,5)
#print l
def mergeSort(array,p,r):
    if p < r:
        q = ( p + r )/2 
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)
mergeSort(l,0,len(l)-1)
print l
"""
if __name__=='__main__':
    params = sys.argv
    if len(params) < 2:
        print "Please enter the array to be sorted"
        sys.exit(0)
    mergeSort([for int(i) in raw_input().split(' ')])
"""
