#!/usr/bin/python

def find_element_by_rank(array, r):
    #print 'trying for rank = {} in array = {}'.format(r, array)
    if len(array) == 1 and r <= 1:
        return array[0]
    groups = createFiveGroups(array)
    #print 'groups are {groups}'.format(groups = groups)
    p = [sorted(k)[len(k)/2] for k in groups]
    approxMedian = find_element_by_rank(p, len(p) / 2 )
    #print 'approxMedian for {array} is {approxMedian}'.format(array= array , approxMedian = approxMedian )
    left = filter(lambda k: k < approxMedian, array )
    right = filter(lambda k: k > approxMedian, array )
    if len(left) == r - 1:
        #print 'here'
        return approxMedian
    if len(left)  >= r :
        #print 'in left with {left}'.format(left = left )
        return find_element_by_rank(left, r)
    else:
        #print 'in right with {right}'.format(right = right )
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
    print find_element_by_rank(input, rank)
