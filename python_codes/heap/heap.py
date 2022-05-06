#!/usr/bin/python

def heapify(seq,maxHeap=True):
    size = len(seq) -1
    for i in range(0,(size/2) + 1):
        if maxHeap:        
            heapify_util_max(seq,size/2-i,size)
        else:
            heapify_util_min(seq,size/2-i,size)

def heapify_util_max(seq,parent,size):
    lson = (parent << 1) + 1
    rson = (parent << 1) + 2
    largest = seq[parent]
    largeIndex = parent
    if lson <= size and  seq[lson] > largest:
        largest = seq[lson]
        largeIndex = lson
    if rson <= size and seq[rson] > largest:
        largest = seq[rson]
        largeIndex = rson
    if largeIndex != parent:    
        swap(seq, parent, largeIndex)
        heapify_util_max(seq,largeIndex,size)

        
def heapify_util_min(seq,parent,size):
    if not seq:
        return
    lson = (parent << 1) + 1
    rson = (parent << 1) + 2
    smallest = seq[parent]
    smallIndex = parent
    if lson <= size and  seq[lson] < smallest:
        smallest = seq[lson]
        smallIndex = lson
    if rson <= size and seq[rson] < smallest:
        smallest = seq[rson]
        smallIndex = rson
    if smallIndex != parent:    
        swap(seq, parent, smallIndex)
        heapify_util_min(seq,smallIndex,size)

def swap(seq, a, b):
    seq[a],seq[b] = seq[b],seq[a]

def heapSort(seq, result):
    if not seq:
        return result
    result.append(seq[0])
    swap(seq, 0, len(seq) -1)
    seq = seq[:len(seq) -1]
    heapify_util_min(seq, 0, len(seq) - 1)
    return heapSort(seq, result)

if __name__ == '__main__':
    #l = [1,2,6,3,13]
    l = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    heapify(l)
    print "max_heap = {l}".format(l=l)
    #l = [1,2,6,3,13]
    #l = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    l = [-10, -7, -9, -5, -7, 2, -6, 2, -8, 8, 10, 5, 4, 9, 3, 8, 3, -2]
    heapify(l,maxHeap = False)
    print "min_heap = {l}".format(l=l)
    result = heapSort(l, [])
    print result
