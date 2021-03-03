#!/usr/bin/python
from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findShortestPathDFS(self, source, dest, seenSoFar = [], bestPath = None):
        seenSoFar = seenSoFar + [source]
        if source == dest:
            return seenSoFar
        for n in self.graph[source]:
            if n not in seenSoFar:
                if bestPath == None or len(seenSoFar) < len(bestPath):
                    newPath = self.findShortestPathDFS(n,dest,seenSoFar,bestPath)
                    if newPath != None:
                        bestPath = newPath
        return bestPath            


def solution(A,B):
    g = Graph()
    for (i,j) in zip(A,B):
        g.addEdge(i,j)
    cities = set(A + B)
    found = True
    for c in cities:
        for d in cities:
            if c == d:
                continue
            else:
                if  g.findShortestPathDFS(d, c) == None:
                    found = False
                    break
        if found:
           return c 
        else:
            found = True
    return -1 


if __name__ == '__main__':
    print solution([0,1,2,4,5], [2,3,3,3,2])
    print solution([1,2,3], [0,0,0])
    print solution([2,3,3,4], [1,1,0,0])

