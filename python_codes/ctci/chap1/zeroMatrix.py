#!/usr/bin/python

def zeroMatrix(matrix):
    rowHasZero = isRowHasZero(matrix) # first row
    colHasZero = isColHasZero(matrix) # first col
    for rowIdx in range(len(matrix)):
        for colIdx in range(len(matrix[rowIdx])):
            if matrix[rowIdx][colIdx] == 0:
                matrix[rowIdx][0] = 0
                matrix[0][colIdx] = 0
    for idx in range(1, len(matrix)):
        if matrix[idx][0] == 0:
            setRowToZero(matrix, idx)
    for idx in range(1, len(matrix[0])):
        if matrix[0][idx] == 0:
            setColToZero(matrix, idx)
    if rowHasZero:
        setRowToZero(matrix, 0)
    if colHasZero:
        setColToZero(matrix, 0)
    return matrix    


def setRowToZero(matrix, idx):
    for colIdx in range(len(matrix[idx])):
        matrix[idx][colIdx] = 0
        

def setColToZero(matrix, idx):
    for rowIdx in range(len(matrix)):
        matrix[rowIdx][idx] = 0

def isRowHasZero(matrix):
    for colIdx in range(len(matrix[0])):
        if matrix[0][colIdx] == 0:
            return True
    return False


def isColHasZero(matrix):
    for rowIdx in range(len(matrix)):
        if matrix[rowIdx][0] == 0:
            return True
    return False


if __name__ == '__main__':
    inputM = [[1,1], [2,2]]
    result = zeroMatrix(inputM)
    assert(result[0] == [1,1])
    assert(result[1] == [2,2])

    inputM = [[1,1], [2,0]]
    result = zeroMatrix(inputM)
    assert(result[0] == [1,0])
    assert(result[1] == [0,0])


    inputM = [[1,1,2], [2,0,3]]
    result = zeroMatrix(inputM)
    assert(result[0] == [1,0,2])
    assert(result[1] == [0,0,0])

    inputM = [[1,1,2], [2,0,3], [4,5,6]]
    result = zeroMatrix(inputM)
    assert(result[0] == [1,0,2])
    assert(result[1] == [0,0,0])
    assert(result[2] == [4,0,6])

    inputM = [[1,1,2], [2,0,3], [0,5,6]]
    result = zeroMatrix(inputM)
    assert(result[0] == [0,0,2])
    assert(result[1] == [0,0,0])
    assert(result[2] == [0,0,0])
