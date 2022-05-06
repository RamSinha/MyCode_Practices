#!/usr/bin/python
class CordNode:
    def __init__(self, weight = 0, chars = []):
        self.left = None
        self.right = None
        self.parent = None
        self.weight = weight
        self.chars = chars
    
    def __repr__(self):
        return ('[ len = {l} and char = {chars} ] '.format(l = self.weight , chars = self.chars ))


class CordTree:
    def __init__(self):
        self.root = None
        self.leafSize = 2
    
    def createCord(self, chars, parent = None):
        
        if len(chars) > self.leafSize:
            #print ('spliting for {chars}'.format(chars = chars))
            leftSplitSize = len(chars) // 2
            leftSplit = chars[:leftSplitSize]
            rightSplit = chars[leftSplitSize :]
            temp = CordNode(leftSplitSize, chars)
            temp.parent = parent
            temp.left  = self.createCord(leftSplit, temp)
            temp.right  = self.createCord(rightSplit, temp)
            return temp
        
        else:
            temp = CordNode(len(chars), chars)
            temp.parent = parent
            return temp


    def printTree(self, top):
        stack = []
        while stack or top:
            while top:
                stack.append(top)
                top = top.left
            top = stack.pop()
            print (top.weight , ','.join(top.chars))
            top = top.right
            
        
    def charAt(self, root, idx):
        if idx < 0:
            raise Exception ('Invalid input')
        if idx >= root.weight and root.right is not None:
            return self.charAt(root.right, idx - root.weight)
        if root.left is not None:
            return self.charAt(root.left, idx)
        if idx >= len(root.chars):
            raise Exception ('Index outof range')
        return root.chars[idx]

    def concat(self, otherCordTreeRoot):
        pass

    def report(self, idxStart, idxEnd):
        pass

    def split(self, idx):
        pass

    def delete(self, idxStart, idxEnd):
        pass


if __name__ == '__main__':
    string = 'mynameisram'
    tree = CordTree()
    root = tree.createCord(list(string))
    tree.printTree(root)
    assert (tree.charAt(root , 0) == 'm')
    assert (tree.charAt(root , 1) == 'y')
    assert (tree.charAt(root , 6) == 'i')
    assert (tree.charAt(root , 10) == 'm')

