#!/usr/bin/python

def insertMtoN(m, n, i, j):
    '''
    we need function to compare ith index of two bit vector
    we need function to toggle ith index in a bit vector if bits in m and n differ at ith index
    '''
    for idx in range(i, j+1):
        maskN = 1 << idx
        maskM = 1 << (idx - i)
        if (m & maskM == 1  and n & maskN == 1) or (m & maskM == 0  and n & maskN == 0):
            continue
        else:
            if n & maskN == 0:
                n |= maskN
            else:
                n &= ~maskN
    print(bin(n))
    print(bin(m))

if __name__ == '__main__':
    insertMtoN(int('10011', 2), int('10000000000', 2), 2 , 6)
