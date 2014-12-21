#!/usr/bin/python

def bubbleSort(array):
    swapped = True
    for i in range(0, len(array)):
        if not swapped:
            print "here"
            break
        for j in range(len(array) -1, i - 1, -1):
            if array[j] < array[j-1]:
                swapped = True
                swap(array, j, j-1)
def swap(array, i, j):
    if array[i] == array[j]:
        return 
    array[i] = array[i] ^ array[j]
    array[j] = array[i] ^ array[j]
    array[i] = array[i] ^ array[j]

if __name__=='__main__':
    input = [int(i) for i in raw_input().split(' ')]
    bubbleSort(input)
    print input
