#!/usr/bin/python

class Node(object):
    def __init__(self, value):
        self.low = min(value)
        self.high = max(value)
        self.max = max(value)
        self.left = None
        self.right = None
    def __repr__(self):
        return f'{self.low}, {self.high}'
       
class IntervalTree(object):
    @staticmethod
    def insertInterval(root, value):
        low = min(value)
        high = max(value)
        if root.low > low:
            if root.left is None:
                root.left = Node(value)
            else:
                IntervalTree.insertInterval(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                IntervalTree.insertInterval(root.right, value)

        root.max = max (root.max, max(value))
        return root
    
    @staticmethod
    def printTree(root):
        if root:
            print(f'{root.low}, {root.high}, {root.max}')
            IntervalTree.printTree(root.left)
            IntervalTree.printTree(root.right)

    @staticmethod
    def findIntervalOverlap(root, interval):
        if root is None:
            return False
        if IntervalTree.doesOverlap(root.low, root.high, interval[0], interval[1]) is True:
            print (root, interval)
            return True
        '''
        if left is not none and max high of left is lower than low if test
        then interval can't match with the left population

        otherwise
        if there is any possible match then  it will be for sure in left subtree
        NOTE: there still may be some in right subtree but we are just looking
        for existance of conflict not all the conflict
        assume the interval with max high is I -> [a, max]
        we know that I[l] < max
        if I[h] > a then there will be conflict
        if I[h] < a then it will never match anyway with any set of right since
        RIGHT[start] > LEFT[start]
        '''
        if root.left is not None and root.left.max > interval[0]:
            return IntervalTree.findIntervalOverlap(root.left, interval)
        return IntervalTree.findIntervalOverlap(root.right, interval)    

    @staticmethod
    def doesOverlap(l1, h1, l2, h2):
        return l1 < h2 and l2 < h1 

if __name__ == '__main__':
    r = Node([5, 20])
    IntervalTree.insertInterval(r, [10, 30])
    IntervalTree.insertInterval(r, [12, 15])
    IntervalTree.insertInterval(r, [15, 20])
    IntervalTree.insertInterval(r, [17, 19])
    IntervalTree.insertInterval(r, [30, 40])
    IntervalTree.insertInterval(r, [3, 4])
    IntervalTree.insertInterval(r, [8, 14])
    IntervalTree.insertInterval(r, [9, 17])
    #IntervalTree.printTree(r)
    print(IntervalTree.findIntervalOverlap(r, [1,3]))
    

