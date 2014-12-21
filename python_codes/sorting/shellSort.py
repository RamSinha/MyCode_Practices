#!/usr/bin/python
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start in range(sublistcount):
        gapInsertionSort(alist,start,sublistcount)
      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        while i>=gap and alist[i-gap]>alist[i]:
            swap(alist,i,i-gap)
            i -= gap
def swap(array, i, j):
    if array[i] == array[j]:
        return 
    array[i] = array[i] ^ array[j]
    array[j] = array[i] ^ array[j]
    array[i] = array[i] ^ array[j]

if __name__=='__main__':
    input = [int(i.strip()) for i in raw_input().split(' ') if i.strip() ]
    shellSort(input)
    print input

