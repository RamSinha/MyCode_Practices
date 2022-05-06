#!/usr/bin/python

# 1,2,1,3,5,6,7,8,9 -> not a valid array, there must always be a mountain in every section
def findPeakInZigZagArray(array):
    def findPeakInZigZagArrayUtil(array, start, end):
        if start == end:
            return array[start]
        if start < end:
            mid = ( start + end ) // 2
            if array[mid] > array[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return findPeakInZigZagArrayUtil(array, start, end)
    return findPeakInZigZagArrayUtil(array, 0, len(array))


if __name__ == '__main__':
    assert (findPeakInZigZagArray([1,2,3,2,-1]) == 3)
    assert (findPeakInZigZagArray([1,2,1,3,5,6,4]) in [1, 6])
