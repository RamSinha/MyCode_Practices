#!/usr/bin/python
def printPattern(rows):
    col = rows
    for i in range(rows):
        for j in range(col):
            print ("*", end = ' ')
        col -= 1    
        print()    
if __name__ == '__main__':
    printPattern(10)
