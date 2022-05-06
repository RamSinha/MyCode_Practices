#!/usr/bin/python
import sys
class Node(object):
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def findAllArrays(root):
    if root is None:
        return []

    leftLists = findAllArrays(root.left)
    rightLists = findAllArrays(root.right)
    result = []
    if not leftLists and not rightLists:
        return [[root.label]]
    if not leftLists:
        return map(lambda r : [root.label] + r, rightLists )
    if not rightLists:
        return map(lambda l : [root.label] + l, leftLists )
    for l in leftLists:
        for r in rightLists:
            weave(l , r , [], result)
    return map(lambda r : [root.label] + r, result )



def weave(left, right, prefix, result):
    if not left:
        result.append(prefix + right)
    elif not right:
        result.append(prefix + left)
    else:
        weave(left[1:], right, prefix + [left[0]], result)
        weave(left, right[1:], prefix + [right[0]], result)


if __name__ == '__main__':
    t = Node(12)
    t.left = Node(7)
    t.right = Node(18)
    t.left.left = Node(5)
    t.left.right = Node(9)
    print findAllArrays(t)

    t = Node(2)
    t.left = Node(1)
    t.right = Node(3)
    print findAllArrays(t)
