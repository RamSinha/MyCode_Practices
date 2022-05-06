#!/usr/bin/python

def printPattern(n):
    rows = 2 * n - 1
    cols = 2 * n - 1
    for r in range(rows):
        for c in range(cols):
            distance = min(c, cols - c - 1, r , rows -r -1)
            print (n - distance, end = ' ')
        print ()

if __name__ == '__main__':
    printPattern(4)
    printPattern(7)
