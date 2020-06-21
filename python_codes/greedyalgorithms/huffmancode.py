#!/usr/bin/python
from queue import PriorityQueue
import copy
class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Pqnode(object):
    def __init__(self,symbol,freq):
        self.symbol = symbol
        self.freq = freq
        self.right = None
        self.left = None
    def __lt__(self,other):
        return self.freq < other.freq
    def __repr__(self):
        return 's:{s} f: {f} l: {l} r: {r}'.format(s=self.symbol, f=self.freq, l=self.left, r=self.right)

def encode(nodes):
    pqueue = PriorityQueue()
    for node in nodes:
        pqueue.put(node)
    for i in range(len(nodes)-1):
        fmin = pqueue.get() 
        smin = pqueue.get()
        n=Pqnode("*", fmin.freq+smin.freq)
        n.left = fmin
        n.right = smin
        pqueue.put(n)
    return pqueue.get()

def printSymbols(node, result=[]):
    
    if node:
        if not node.left and not node.right:
            print 'symbol: {s} encoding: {e}'.format(s=node.symbol,e=''.join(result))
        else:    
            llocal = result + ['0']
            rlocal = result + ['1']
            printSymbols(node.left, llocal)
            printSymbols(node.right, rlocal)


if __name__ == '__main__':
    freq = '45,13,12,16,9,5'
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    chars = raw_input('Enter symbols: ex = {ex}\n'.format(ex=','.join(chars))).split(",")
    freq = map(lambda x: int(x), raw_input('Enter freq: ex = {ex}\n'.format(ex=freq)).split(","))
    assert(len(freq) == len(chars))
    nodes = map(lambda (x,y): Pqnode(x,y), zip(chars, freq))
    root = encode(nodes)
    printSymbols(root)

