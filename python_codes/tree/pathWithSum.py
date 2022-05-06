#!/usr/bin/python

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathWithSum(root, target, paths):
    if root is not None:
        pathWithSumUtil(root, target, paths)
        pathWithSum(root.left, target, paths)
        pathWithSum(root.right, target, paths)

    return paths

     
def pathWithSumUtil(root, target, paths, currentPath = []):
    if root is None:
        return
    if target - root.data  == 0:
        paths.append(currentPath + [root.data])
    pathWithSumUtil(root.left, target - root.data, paths, currentPath + [root.data])
    pathWithSumUtil(root.right, target - root.data, paths, currentPath + [root.data])

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


