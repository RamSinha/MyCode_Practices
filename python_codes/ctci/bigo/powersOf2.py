#!/usr/bin/python

def powersOf2(n):
    #base case
    if n < 1:
        print(0, end = ' ') # printing 2^0 = 1
        return 0
    if n == 1:
        print(1, end = ' ') # printing 2^0 = 1
        return 1
    else:
        prev = powersOf2(n // 2) # recurse on smaller prob
        curr = prev * 2 # use sol of smaller prob and solve big problem
        print(curr, end = ' ')
        return curr

if __name__ == '__main__':
    powersOf2(10000)
    print('')
    powersOf2(10001)
    print('')
    powersOf2(10002)
    print('')
    powersOf2(10003)
    print('')
    powersOf2(10004)
    print('')
    powersOf2(10005)
    print('')
    powersOf2(20000)
    print('')
