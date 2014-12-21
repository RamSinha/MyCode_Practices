#!/usr/bin/python
def quickSort(array, left, right):
    if left >= right:
        return
    last = (left + right)/2
    swap (array, left, (left+right)/2)
    last = left
    for i in range(left+1,right+1):
        if array[i] <= array[left]:
            last += 1
            swap (array, last, i)
    swap(array, left, last)
    quickSort(array,left, last-1)
    quickSort(array, last+1, right)

def swap(array, i, j):
    if array[i] == array[j]:
        return 
    array[i] = array[i] ^ array[j]
    array[j] = array[i] ^ array[j]
    array[i] = array[i] ^ array[j]

if __name__=='__main__':
    input = [int(i) for i in raw_input().split(' ')]
    quickSort(input,0, len(input)-1)
    print input
