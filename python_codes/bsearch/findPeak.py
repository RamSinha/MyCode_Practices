#!/usr/bin/python

def findPeak_m(array):
    start = 0
    end = len(array) -1
    while start < end:
        mid = (start + end) // 2
        if array[mid] > array[mid+1]: # no need to check for outofbound, since s < e
            end = mid
        else:
            start = mid + 1
    return end


def findPeak(array):
    if not array:
        return -1
    if len(array) == 1:
        return array[0]

    start = 0
    end = len(array) -1
    while start < end:
        mid = ( start + end ) // 2 
        if array[mid] > array[mid+1]:
            end = mid
        else:
            start = mid + 1
    return start        

if __name__ == '__main__':
    assert(findPeak([1,2,23,34,5,3]) == 3)
    assert(findPeak_m([1,2,23,34,5,3]) == 3)
