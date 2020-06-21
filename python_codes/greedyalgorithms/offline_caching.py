#!/usr/bin/python
from collections import defaultdict
import sys
class Node(object):

    def __init__(self, name):
        self.name = name
        self.next = None
        self.ni = sys.maxint

    def nnext(self):
        return self.next
    
    def setNext(self, node):
        self.next = node
    
    def setNextIndex(self, nextIndex):
        self.ni = nextIndex

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()
    
    def __repr__(self):
        return self.name + '-->' + str(self.ni)


def processSchedule(schedule):
    lookup = dict()
    start = Node('head')
    for i,s in enumerate(schedule):
        if s not in lookup:
            lookup[s] = s
        else:
            lookup[s].setNextIndex(i)
            lookup[s] = s

def applyCachingStrategy(processedSchedule, k):
    cache = []
    print processedSchedule
    for s in processedSchedule:
        if s in cache:
            print 'hit {}'.format(s.name)
            cache[cache.index(s)]=s 
        else:
            if s.ni == sys.maxint:
                print 'miss {} do nothing'.format(s.name)
            elif len(cache) < k:
                print 'miss {} insert '.format(s.name, s.name)
                cache = cache + [s]    
            else:
                maxIndex = 0
                maxV = 0
                for i,e in enumerate(cache):
                    if maxV < e.ni:
                        maxIndex = i
                        maxV = e.ni
                if s.ni < maxV:
                    print 'miss {}'.format(s.name)
                    print 'insert {} evict {}'.format(s.name,cache[maxIndex].name)
                    cache[maxIndex] = s 
                else:
                    print 'miss {} but do nothing'.format(s.name)

if __name__ == '__main__':
    s = map(lambda x: Node(x), raw_input('Enter the cache schedule, ex: a,b,c,d,e,f,a,b\n').split(','))
    cacheSize = int(raw_input('Enter the cache size (valid integer)'))
    processSchedule(s)     
    applyCachingStrategy(s,cacheSize)
