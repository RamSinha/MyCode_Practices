def spiralTraverse(array):
    # Write your code here.
    if not array:
        return array
    result = printArrayUtil(array, 0, len(array)-1, 0, len(array[0]) -1, [])
    return result


def printArrayUtil(array, iLower, iUpper, jLower, jUpper, result):
    if (iLower > iUpper) or (jLower > jUpper):
        return []
    i, j = iLower, jLower
    # Left to Right
    while (j <= jUpper):
        result.append(array[i][j])
        j += 1
    i = iLower + 1
    j = jUpper
    # Right top to Bottom
    while (i <= iUpper):
        result.append(array[i][j])
        i += 1
    j = jUpper -1
    i = iUpper
    # Right to left
    while (j >= jLower and iLower != iUpper):
        result.append(array[i][j])
        j -= 1
    i = iUpper - 1
    j = jLower
    # Bottom left to up
    while (i > iLower and jLower != jUpper):
        result.append(array[i][j])
        i = i - 1
    remaining = printArrayUtil(array, iLower + 1, iUpper - 1, jLower + 1, jUpper - 1, [])
    result.extend(remaining)
    return result

if __name__ == '__main__':
    array =  [[1]]
    print (spiralTraverse(array))

