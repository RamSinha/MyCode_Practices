#!/usr/bin/python

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathWithSum(root, target, currentSum, cache = {}):
    if root is None:
        return 0
    runningSum = currentSum + root.data
    targetSum = target - runningSum
    totalPaths = 0 if targetSum not in cache else cache[targetSum]

if __name__ == '__main__':
    t = Tree(10)
    t.left = Tree(5)
    t.left.left = Tree(3)
    t.left.left.left = Tree(3)
    t.left.left.right = Tree(-2)
    t.left.right = Tree(2)
    t.left.right.right = Tree(1)
    t.right = Tree (-3)
    t.right.right = Tree (11)
    #paths = pathWithSum(t, 8, [])
    #print (paths)
    paths = pathWithSum(t, 11, [])
    print (paths)


