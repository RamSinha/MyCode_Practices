#!/usr/bin/python

def searchInMountainArray(array, target):
    def searchInMountainArrayUtil(array, start, end, target):
        if start > end:
            return -1
        if start == end:
            return array[start] == target
        mid = ( start + end ) // 2
        if array[mid] == target:
            return True
        if array[mid] > array[mid + 1]:
            if array[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if array[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return searchInMountainArrayUtil(array, start, end, target)
    return searchInMountainArrayUtil(array, 0, len(array), target)



if __name__ == '__main__':
    assert(searchInMountainArray([1,5,3], 5) == True)
    assert(searchInMountainArray([1,5,3], 6) == False)
    assert(searchInMountainArray([1,5,3,2,1,-1], 2) == True)
    assert(searchInMountainArray([45, 61, 71, 72, 73, 0, 1, 21, 33, 37],  33) == True)
