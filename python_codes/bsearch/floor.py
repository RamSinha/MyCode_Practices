#!/usr/bin/python
'''
Greatest number smaller than the target.
'''
def findFloor(array, target):
    def findFloorUtil(array, target, start, end):
        if start > end:
            return end
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
        return findFloorUtil(array, target, start, end)
    return findFloorUtil(array, target, 0, len(array) -1)


if __name__ == '__main__':
    assert(findFloor ([3,9,11,18,21], 17) == 2)
    assert(findFloor ([3,9,11,18,21], 18) == 3)
    assert(findFloor ([3,9,11,18,21], 18) == 3)
    assert(findFloor ([3,9,11,18,21], 2) == -1)
    assert(findFloor ([3,9,11,18,21], 22) == 4)
