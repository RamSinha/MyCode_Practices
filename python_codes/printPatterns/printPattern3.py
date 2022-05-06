#!/usr/bin/python
def printPattern(rows):
    col = 0
    for i in range(rows):
        col += 1
        for j in range(1,col+1):
            print (j, end = ' ')
        print()    
if __name__ == '__main__':
    printPattern(10)
