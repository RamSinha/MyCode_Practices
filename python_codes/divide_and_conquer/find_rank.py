#!/usr/bin/python

def find_element_by_rank(array, r):
    if len(array) == 1 and r <= 1:
        return array[0]
    groups = createFiveGroups(array)
    p = [sorted(k)[len(k)/2] for k in groups]
    approxMedian = find_element_by_rank(p, len(p) / 2 )
    left = filter(lambda k: k < approxMedian, array )
    right = filter(lambda k: k > approxMedian, array )
    if len(left) == r - 1:
        return approxMedian
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
    input = map(lambda x : int(x), raw_input("please enter element array, ex: 1,2,3,4\n").split(','))
    rank = int(raw_input("please enter element rank to find "))
    if len(input) < rank:
        raise Exception('''In valid input, rank can't be more than length of dataset''')
    print find_element_by_rank(input, rank)
