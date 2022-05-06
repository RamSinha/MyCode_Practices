#!/usr/bin/python

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createLinkedListsFromTree(root, lists = [], level = 0):
    if root is None:
        return lists
    if len(lists) == level:
        lists.append([])
    lists[level].append(root.data)
    createLinkedListsFromTree(root.left, lists, level + 1 )
    createLinkedListsFromTree(root.right, lists, level + 1 )
    return lists

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
    paths = createLinkedListsFromTree(t)
    print (paths)


