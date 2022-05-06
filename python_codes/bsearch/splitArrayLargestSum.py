#!/usr/bin/python

def splitArrayLargestSum(array, m):
    def splitArrayLargestSumUtil(array, m, s, e):
        if s >= e:
            return e
        p = (s + e) // 2 
        parts = 1
        sum_r = 0 # running sum
        for i in array:
            if sum_r + i > p:
                sum_r = i
                parts = parts + 1
            else:
                sum_r += i
        if parts > m:
            s = p + 1 
        else:
            e = p
        return splitArrayLargestSumUtil(array, m , s , e )
    return splitArrayLargestSumUtil(array, m, max(array), sum(array))

if __name__ == '__main__':
    print (splitArrayLargestSum([7,2,5,10,8], 2))
