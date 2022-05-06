#!/usr/bin/python

import random

class Tree (object):
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None
   
    def insertInorder(self, data):
        if self.data < data:
            if self.left is None:
                self.left = Tree (data)
            else:
                self.left.insertInorder(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insertInorder(data)
        self.size = self.size + 1
       
    def findNode(self, data):
        if self.data == data:
            return self
        elif self.data > data:
            return None if self.left is None else self.left.findNode(data)
        else:
            return None if self.right is None else self.right.findNode(data)

    def getRandomNode(self):
        leftSize = 0 if self.left is None else self.left.size
        idx = random.randint(1, self.size)
        if idx == leftSize + 1:
            return self
        elif idx <= leftSize:
            return self.left.getRandomNode()
        else:
            return self.right.getRandomNode()

    def getRandomNodeOptimized(self):
        idx = random.randint(1, self.size)

        def getRandomNodeOptimizedUtil(root, position):
            leftSize = 0 if self.left is None else self.left.size
            if position == leftSize + 1:
                return root
            if position <= leftSize:
                return getRandomNodeOptimizedUtil(root.left, position)
            else:
                return getRandomNodeOptimizedUtil(root.right, position - (leftSize + 1) )
        return getRandomNodeOptimizedUtil(self, idx)

if __name__ == '__main__':
    a = [5,1,7,8]
    iteration =  1000000
    d = {}
    t = Tree(3)
    for i in a:
        t.insertInorder(i)
    for k in range(iteration):
        result = t.getRandomNode().data
        if result not in d:
            d[result] = 0
        d[result] += 1
    for (k,v) in d.items():
        print (k, v / iteration)

    d = {}
    print('******* OPTIMIZED *******')
    for k in range(iteration):
        result = t.getRandomNode().data
        if result not in d:
            d[result] = 0
        d[result] += 1
    for (k,v) in d.items():
        print (k , v / iteration)
