#!/usr/bin/python

def findKSubSet(array, k):
    if sum(array) % k != 0:
        raise Exception ('Invalid input')
    target = [sum(array) // 3] * k
    result = [[] for _ in range(k)]
    def findKSubSetUtil(array, idx, result, target):
        if idx < len(array):
            for bucketIdx in range(len(target)):
                currentValue = array[idx]
                if (currentValue <= target[bucketIdx]):
                    target[bucketIdx] -= currentValue
                    if (findKSubSetUtil(array, idx + 1, result, target)):
                        result[bucketIdx].append(currentValue)
                        break
                    else:
                        target[bucketIdx] += currentValue
        return sum(target) == 0
    findKSubSetUtil(array, 0, result, target)
    return result, target 

if __name__ == '__main__':
    array = [4,2,3,6,3,1,5]
    print (findKSubSet(array, 3))
