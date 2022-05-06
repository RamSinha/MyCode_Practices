#!/usr/bin/python
def printPattern(rows):
    col = rows
    rows = 2 * rows + 1 
    for i in range(rows):
        if col is 0:
            print ('- ' * (rows // 2) , end = '')
        for j in range(col):
            print ("*", end = ' ')
        if i < (rows // 2):
            col -= 1
        else:
            col += 1
        print()    
if __name__ == '__main__':
    printPattern(5)
