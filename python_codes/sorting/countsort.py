#!/usr/bin/python

def countSort(array, count):
    c = [0 for _ in range(count+1)]
    for i in array:
        c[i] +=1
    # element less than OR equal to idx    
    for i in range(1, len(c)):
        c[i] = c[i-1] + c[i]
    print (c)    
    b = [None for _ in range(len(array))]
    # reverse iteration will result in stable sort
    for i in reversed(range(len(array))):
        b[c[array[i]]-1] = array[i]
        c[array[i]] -=1
    return b    

if __name__ == '__main__':
    array = map( lambda x : int(x), raw_input('Input the array: ex: {}\n'.format('13,1,5,10')).split(','))
    print ('sorted result is: \n{}'.format(countSort(array, max(array))))

