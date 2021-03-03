#!/usr/bin/python
from collections import defaultdict
import inspect

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.value)

    def printLevelOrderUsingTwoQ(self):
        print '\n' + inspect.currentframe().f_code.co_name +'\n'
        lookup = defaultdict(list)
        q1=[]
        q2=[]
        q1.append(self)
        while (q1 or q2):
            for i in q1:
                print i.value, 
                if i.left:
                    q2.append(i.left)
                if i.right:
                    q2.append(i.right)
            print '\n'
            q1 = q2
            q2 = []
    
    def printLevelOrder(self):
        print '\n' + inspect.currentframe().f_code.co_name +'\n'
        q=[]
        q.append(self)
        while q:
            count = len(q)
            while (count > 0):
                top = q[0]
                q = q[1:]
                print top,
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                count = count -1
            print '\n'    
     
    def printLevelOrderSpecialChar(self):
        print '\n' + inspect.currentframe().f_code.co_name +'\n'
        q = []
        q.append(self)
        while q:
            q.append(None)
            while True:
                top = q[0]
                q = q[1:]
                print top,
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                if not q[0]: 
                    q=q[1:]
                    break
            print '\n'        


    def printTreeVertical(self):
        print '\n' + inspect.currentframe().f_code.co_name +'\n'
        lookup = defaultdict(list)
        def printTreeVerticalHelper(node,distance):
            if node:
                lookup[distance].append(node)
                printTreeVerticalHelper(node.left, distance-1)
                printTreeVerticalHelper(node.right, distance+1)
        printTreeVerticalHelper(self,0)
        for k in sorted(lookup):
            print lookup[k]


    def printTreeVerticaUsingLevelOrder(self):
        print '\n' + inspect.currentframe().f_code.co_name +'\n'
        lookup = defaultdict(list)
        q=[]
        q.append((self,0))
        while q:
            count = len(q)
            while count > 0:
                (top,d) = q[0]
                lookup[d].append(top)
                q = q[1:]
                if top.left:
                    q.append((top.left,d-1))
                if top.right:
                    q.append((top.right,d+1))
                count = count - 1     
        for k in sorted(lookup):
            print lookup[k]



if __name__ == '__main__':
    t = Node(10)
    t.left = Node(5)
    t.right = Node(12)
    t.left.left = Node(3)
    t.left.right = Node(9)
    t.right.left = Node(11)
    t.right.right = Node(15)
    t.left.right.left = Node(19)
    t.left.right.right = Node(29)
    t.right.right.left = Node(25)
    t.right.right.right = Node(35)
    t.printLevelOrderUsingTwoQ()
    t.printLevelOrder()
    t.printLevelOrderSpecialChar()
    t.printTreeVertical()
    t.printTreeVerticaUsingLevelOrder()

