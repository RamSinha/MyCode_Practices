#!/usr/bin/python

def radixSort(array):
    if not array:
        return array
    maxElem = max(array)
    digit = 0
    while maxElem // 10 ** digit > 0:
        countSortAtDigit(array, digit)
        digit += 1
    return array

def countSortAtDigit(array, digit):
    counter = [0 for _ in range(10)] # base 10 will have entries 0 .. 9
    copy = [None for _ in array]
    for e in array:
        valueAtDigit = (e // 10 ** digit) % 10
        counter[valueAtDigit] += 1

    for idx in range(1,10):
        counter[idx] += counter[idx -1]

    for e in array[::-1]:
        digitIdx = (e // 10 ** digit) % 10
        copy[counter[digitIdx] -1] = e
        counter[digitIdx] -= 1

    for idx in range(len(array)):
        array[idx] = copy[idx]
    return array    

if __name__ == '__main__':
    assert (radixSort( [8762, 654, 3008, 345, 87, 65, 234, 12, 2] ) == [2, 12, 65, 87, 234, 345, 654, 3008, 8762])  
