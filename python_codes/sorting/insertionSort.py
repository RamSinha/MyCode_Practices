#!/usr/bin/python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key

if __name__ == '__main__':
    inputArray = [int (i) for i in raw_input('Enter elements ex: 9 1 7 13 -1 \n').split(' ')]
    insertion_sort(inputArray)
    print (inputArray)
