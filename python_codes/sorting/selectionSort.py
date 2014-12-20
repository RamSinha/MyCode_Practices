#!/usr/bin/python
def selectionSort(array):
    for i in range(len(array) - 1, 0, -1 ):
        large = array[0]
        index = 0
        for j in range(0,i + 1 ):
            if array[j] > large:
                large = array[j]
                index = j
        swap(array,index,i)

def swap(array, i, j):
    if i == j:
        return 
    array[i] = array[i] ^ array[j]
    array[j] = array[i] ^ array[j]
    array[i] = array[i] ^ array[j]

if __name__=='__main__':
    input = [int(i.strip()) for i in raw_input().split(' ') if i.strip() ]
    selectionSort(input)
    print input
