#!/usr/bin/python

def findPivotInRotatedArray(array):
    if not array:
        raise Exception('Invalid input')
    if array[-1] > array[0]:
        return array[-1]

    def findPivotInRotatedArrayUtil(array, start, end):
        if start >= end:
            return array[start]
        mid = ( start + end ) // 2
        if array[mid] > array[mid + 1]:
            return array[mid]
        if array[mid] > array[start]:
            start = mid + 1
        else:
            end = mid
        return findPivotInRotatedArrayUtil(array, start, end)
    return findPivotInRotatedArrayUtil(array, 0, len(array) -1)

if __name__ == '__main__':
    assert(findPivotInRotatedArray([3,4,5,6,7,0,1,2]) == 7)
    assert(findPivotInRotatedArray([3, 4, 1]) == 4)
    assert(findPivotInRotatedArray([3, 4]) == 4)
    assert(findPivotInRotatedArray([2, 9, 2, 2, 2]) == 9)
    assert(findPivotInRotatedArray([2, 2, 2, 2, 2]) == 2)
