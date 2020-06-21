#!/usr/bin/python
def rangeBitwiseAnd(m, n):
    shift = 0   
    # find the common 1-bits
    while m < n:
        m = m >> 1
        n = n >> 1
        shift += 1
    return m << shift
if __name__ == '__main__':
    m = int(raw_input())
    n = int(raw_input())
    print rangeBitwiseAnd(m,n)
