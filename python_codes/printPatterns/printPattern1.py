#!/usr/bin/python
def printPattern(rows):
    col = 0
    for i in range(rows):
        col += 1
        for j in range(col):
            print ("*", end = ' ')
        print()    
if __name__ == '__main__':
    printPattern(10)
