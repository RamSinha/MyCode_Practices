#!/usr/bin/python

def find_min_max(array, left , right):
    if not array:
        raise Exception('Invalid input')
    if left >= right -1:
        c1 = array[left]
        c2 = array[right]
        return (c1, c2) if c1 < c2 else (c2,c1)
    mid = left + (right - left ) / 2 
    (ml, xl) =  find_min_max (array, left, mid)
    (mr, xr) =  find_min_max (array, mid, right)
    if ml < mr:
        result = (ml, xr if xr > xl else xl)
        return result
    else:    
        result = (mr, xr if xr > xl else xl)
        return result


if __name__ == '__main__':
    input = map(lambda x : int(x), raw_input('Enter the list of integers, ex : 1,2,3,4 \n').split(','))
    print find_min_max(input,0, len(input) -1 )
