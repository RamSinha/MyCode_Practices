#!/usr/bin/python


def heapUtil(heap, parentIdx, limit):
    while parentIdx <= limit:
        indexToSwap = parentIdx
        firstChildIdx = parentIdx * 2  + 1
        secondChildIdx = firstChildIdx + 1
        if firstChildIdx <= limit and heap[firstChildIdx] < heap[indexToSwap]:
            indexToSwap = firstChildIdx
        if secondChildIdx <= limit and heap[secondChildIdx] < heap[indexToSwap]:
            indexToSwap = secondChildIdx
        if indexToSwap == parentIdx:
            return
        swap(heap, indexToSwap, parentIdx)
        parentIdx = indexToSwap


def createHeap(array):
    firstParentIdx = ( len(array) -1 -1 )// 2 
    for idx in range(firstParentIdx + 1)[::-1]:
        heapUtil(array, idx, len(array) -1)

def swap(array, i, j):
    if array[i] == array[j]:
        return
    array[i] = array[i] ^ array[j]
    array[j] = array[i] ^ array[j]
    array[i] = array[i] ^ array[j]
    return

def sort(heap):
    createHeap(heap)
    for idx in range(1, len(heap))[::-1]:
        swap(heap, 0, idx)
        heapUtil(heap, 0, idx -1)
    return heap[::-1] 

if __name__=='__main__':
    inputArray = [int(i) for i in raw_input().split(' ')]
    print(sort(inputArray))


