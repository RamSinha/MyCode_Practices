#!/usr/bin/python
def printPattern(rows):
    col = 0
    for i in range(rows):
        if i <= (rows // 2):
            col += 1
        else:
            col -= 1
        for j in range(col):
            print ("*", end = ' ')
        print()    
if __name__ == '__main__':
    printPattern(19)
