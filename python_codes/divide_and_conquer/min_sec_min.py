#!/usr/bin/python

import copy

class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
     
    def __lt__(self, other):
        return self.val < other.val
        
    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

def min_sec_min(array):
    winners = []
    while len(winners) != 1:
        winners  = []
        while array:
            if len(array)>=2:
                c1 = array[0]
                c2 = array[1]
                if c1 < c2:
                    n = Node(c1.val)
                    n.left = c2
                    n.right= c1
                    winners.append(n)
                else:
                    n = Node(c2.val)
                    n.left = c1
                    n.right= c2
                    winners.append(n)
                array = array[2:] 
                    
            else:
                winners.extend(array)
                array = array[1:]
        array = winners
    firstMin = winners[0]
    minimum = firstMin
    secondLevelCandidate = []
    while (minimum.left and minimum.right):
        secondLevelCandidate.append(minimum.left)
        minimum = minimum.right
    if secondLevelCandidate:
        return (firstMin, min(secondLevelCandidate))
    return  (firstMin, firstMin)        
            

        


if __name__ == '__main__':
    input = map(lambda x: Node(int(x)), raw_input('Please enter input ex: 1,2,3,4\n').split(','))
    print min_sec_min(input)
