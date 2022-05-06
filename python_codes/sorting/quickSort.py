#!/usr/bin/python
def quickSort(array, left, right):
    # base case -> left == right mean single element
    #           -> left > right mean empty array
    if left >= right:
        return
    '''
    Any element on left side of last is smaller than pivot
    last refer to position where any smaller element shall be
    placed.
    '''
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
    inputArray = [int(i) for i in raw_input().split(' ')]
    quickSort(inputArray,0, len(inputArray)-1)
    print inputArray
