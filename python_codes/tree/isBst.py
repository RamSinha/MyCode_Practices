#!/usr/bin/python
import sys
class Node(object):
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def isBSTInOrder(root, prev = {}):
    if root is None:
        return True
    res = isBSTInOrder(root.left, prev)
    if res is False:
        return res
    if "prev" in prev:
        if prev["prev"].label > root.label:
            return False
    prev["prev"] = root
    return isBSTInOrder(root.right, prev)


def isBstUtil(root, lRange=-sys.maxsize-1, rRange=sys.maxsize):
    if not root:
        return True
    if root.label > lRange and root.label < rRange:
        return isBstUtil(root.left, lRange, root.label) \
               and isBstUtil(root.right, root.label, rRange)
    else:
        return False

if __name__ == '__main__':
    t = Node(10)
    t.left = Node(5)
    t.right = Node(12)
    t.left.left = Node(3)
    t.left.right = Node(9)
    t.right.left = Node(11)
    t.right.right = Node(15)
    print (isBstUtil(t))
    print (isBSTInOrder(t))
