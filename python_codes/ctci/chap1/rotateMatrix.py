#!/usr/bin/python
def rotateMatrix(matrix):
    '''
    1 2 3                          7 4 1
    4 5 6  ==[90 deg clockwise]==> 8 5 2
    7 8 9                          9 6 3
    '''
    # i, j => j , N - i -1
    N = len(matrix)
    result = [[None for _ in r ] for r in matrix]
    for rowIdx in range(len(matrix)):
        for colIdx in range(len(matrix[rowIdx])):
            result[colIdx][N -rowIdx -1] = matrix[rowIdx][colIdx]
    return result        


def rotateMatrixInPlace(matrix):
    N = len(matrix)
    for layer in range(N / 2):
        for idx in range(layer, N -layer -1):
            top = matrix[layer][idx] # save top 
            matrix[layer][idx] = matrix[N - idx -1][layer] # left to top
            matrix[N - idx -1][layer] = matrix[N -layer -1][N -idx -1] # bottom to left
            matrix[N -layer -1][N -idx -1] = matrix[idx][N - layer -1] # right to bottom
            matrix[idx][N - layer -1] = top # saved top to right
    return matrix

if __name__ == '__main__':
    inputMatix = [[1,2,3], [4,5,6], [7,8,9]]
    expectedOutput = rotateMatrix(inputMatix)
    assert(expectedOutput[0] == [7,4,1])
    assert(expectedOutput[1] == [8,5,2])
    assert(expectedOutput[2] == [9,6,3])
    assert(rotateMatrix([[0]]) == [[0]])
    assert(rotateMatrix([[1]]) == [[1]])
    assert(rotateMatrix([[1,1], [1,1]]) == [[1,1], [1,1]])

    # check inplace rotation
    inputMatix = [[1,2,3], [4,5,6], [7,8,9]]
    expectedOutput = rotateMatrixInPlace(inputMatix)
    assert(expectedOutput[0] == [7,4,1])
    assert(expectedOutput[1] == [8,5,2])
    assert(expectedOutput[2] == [9,6,3])
    assert(rotateMatrixInPlace([[0]]) == [[0]])
    assert(rotateMatrixInPlace([[1]]) == [[1]])
    assert(rotateMatrixInPlace([[1,1], [1,1]]) == [[1,1], [1,1]])
