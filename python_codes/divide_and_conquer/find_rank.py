#!/usr/bin/python

def find_element_by_rank(array, r):
    # every iteration length of array decreases by factor of 1/4, so ultimately it can goes lowest to 1
    if len(array) == 1:
        return array[0]
    groups = createFiveGroups(array)
    p = [sorted(k)[len(k)//2] for k in groups]
    # approxMedian by definition can't largest element unless the size of array is ONE
    # n/4 <= rank(am) <= 3n/4
    approxMedian = find_element_by_rank(p, len(p) // 2 )
    left = list(filter(lambda k: k < approxMedian, array ))
    right = list(filter(lambda k: k > approxMedian, array ))
    if len(left) == r - 1:
        return approxMedian # rank of approx median is the requested rank
    if len(left)  >= r :
        return find_element_by_rank(left, r)
    else:
        return find_element_by_rank(right, r - len(left) - 1)
    
def createFiveGroups(array):
    groups = []
    while array:
        groups.append(array[0:5])
        array = array[5:]
    return groups
if __name__ == '__main__':
    userInput = list(map(lambda x : int(x), input("please enter element array, ex: 1,2,3,4\n").split(',')))
    rank = int(input("please enter element rank to find "))
    if len(userInput) < rank:
        raise Exception('''In valid input, rank can't be more than length of dataset''')
    print (find_element_by_rank(userInput, rank))
