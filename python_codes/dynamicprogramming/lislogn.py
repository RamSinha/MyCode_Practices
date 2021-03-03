#!/usr/bin/python
def findLisLength(array):
    if not array:
        return -1
    b = [float('inf') for _ in range(len(array))]
    b[0] = array[0]
    for i in range(1, len(array)):
        k = findLowerBound(b, array[i])
        #print ('b = {}, a = {}, k = {}'.format(str(b), array[i], k))
        b[k] = array[i]
    return len(filter(lambda x : x != float('inf'), b))

def findLowerBound(array, target):
    i=0
    j=len(array) -1
    if array[i] > target:
        return i
    while (j - i > 1):
        mid = i + ( j - i ) / 2 
        #print ('i = {}, j = {}, mid = {}'.format(i,j, mid))
        if array[mid] <= target:
            i = mid
        else:
            j = mid
    #print ('array = {}, target = {}, j = {}'.format(array, target, j))
    return j

if __name__ == '__main__':
    #print (findLowerBound([0,3,6,8, float('inf')], 5))
    #print (findLowerBound([0,4, float('inf'), float('inf'), float('inf')], 12))
    array = map(lambda x: int(x),raw_input('Please enter integer seq ex: 0,8, 4 , 12, 2\n').split(','))
    print ('Max length of LIS is {} '.format(findLisLength(array)))

