#!/usr/bin/python

class UnionFind(object):
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, vertex):
        v = vertex
        if v not in self.parent:
            self.parent[v] = v
            self.rank[v] = 1
        while v != self.parent[v]:
            v = self.parent[v]
        self.parent[vertex] = v
        return self.parent[vertex]

    def add(self, u, v):
        if self.find(u) != self.find(v):
            if self.rank[self.parent[u]] <= self.rank[self.parent[v]]:
                self.rank[self.parent[v]] += self.rank[self.parent[u]]
                self.parent[self.parent[u]] = self.parent[v]
            else:
                self.rank[self.parent[u]] += self.rank[self.parent[v]]
                self.parent[self.parent[v]] = self.parent[u]

class Union:
    def __init__(self, vertexes):
        self.vertexes = [i for i in range(vertexes)] # holds parent pointer
        self.lookup = dict([(i,0) for i in range(vertexes)]) # holds rank 
    
    def find(self, vertex):
        v = vertex
        while (v != self.vertexes[v]):
            v = self.vertexes[v]
        self.vertexes[vertex] = v # path compression
        return v

    def union(self, first, second):
        firstComponent = self.find(first)
        secondComponent = self.find(second)
        if self.lookup[firstComponent] >= self.lookup[secondComponent]: # union by rank
            self.vertexes[secondComponent] = firstComponent
            self.lookup[firstComponent] = self.lookup[firstComponent] + self.lookup[secondComponent] + 1
        else:
            self.vertexes[firstComponent] = secondComponent
            self.lookup[secondComponent] = self.lookup[secondComponent] + self.lookup[firstComponent] + 1


if __name__ == '__main__':
    u = Union(7)
    print (u.vertexes)
    print (u.lookup)
    u.union(1,3)
    u.union(1,4)
    u.union(5,6)
    u.union(4,5)
    u.union(0,2)
    u.find(6)
    print (u.vertexes)
    print (u.lookup)
    print (u.find(6) == u.find(3))
