#!/usr/bin/python

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createLinkedListsFromTreeUsingBFS(root, lists = []):
    if root is None:
        return lists
    q = [root]
    while q:
        level = []
        for n in q:
            if n.left is not None:
                level.append(n.left)
            if n.right is not None:
                level.append(n.right)
        lists.append(list(map(lambda x : x.data , q)))
        q = level
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
    paths = createLinkedListsFromTreeUsingBFS(t)
    print (paths)


