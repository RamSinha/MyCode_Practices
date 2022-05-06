#!/usr/bin/python


def findCeiling(array, target):
    def findCeilingUtil(array, target, start, end):
        if start > end:
            return start
        mid = (start + end ) // 2
        if array[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return findCeilingUtil(array, target, 0, len(array) -1)

def findIndex(s,pivot,start,end):
    '''
    Modified binary search to return index for mininum value greater than pivot
    for the first time start shall be -1
    '''
    while end - start > 1:  
        mid = end + (start - end) / 2 
        if s[mid] >= pivot:
            end = mid
        else:
            start = mid
    #print "s={s}, pivot={pivot},start={start},end={end}".format(s=s,pivot=pivot,start=start,end=end)        
    return end        


def findIndexGEq(array, target, start, end):

    #base case
    if start > end:
        return start

    mid = ( start + end ) // 2
    if array[mid] >= target:
        end = mid - 1
    else:
        start = mid + 1
    return findIndexGEq(array, target, start, end) 

if __name__ == '__main__':
    inputSeq = map(lambda x : int(x), raw_input('enter the sorted sequence ex: 3,13,15,17 \n').split(","))
    valueToSearchFor = int(raw_input('enter the element \n'))
    #print findIndex(inputSeq, valueToSearchFor, -1 , len(inputSeq))
    print findIndexGEq(inputSeq, valueToSearchFor, 0 , len(inputSeq) -1)
