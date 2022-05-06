#!/usr/bin/python

def monotonicIncreasingQueue(array):
    stack = []
    rightSmaller = [-1] * len(array)
    leftSmaller = [-1] * len(array)
    for idx in range(len(array)):
        while stack and array[stack[-1]] >= array[idx]:
            rightSmaller[stack[-1]] = array[idx]
            stack.pop()
        if stack:
            leftSmaller[idx] = array[stack[-1]]
        stack.append(idx)
    print (array)    
    print (leftSmaller)
    print (rightSmaller)
    return rightSmaller


if __name__ == '__main__':
    assert(monotonicIncreasingQueue([5,3,1,2,4]) == [3,1,-1,-1,-1])
