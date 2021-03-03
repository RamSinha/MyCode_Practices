#!/usr/bin/python
from collections import defaultdict

class Node(object):

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self, s, result):
        queue = []
        visited = defaultdict(bool)
        queue.append(s)
        while queue:
            q = queue.pop(0)
            if not visited[q]:
                result.append(q)
                for e in self.graph[q]:
                    queue.append(e)
                visited[q]=True
        return result        

    def dfs(self,s,result):
        def dfs_util(start, graph, visited, result):
            if not visited[start]:
                result.append(start)
                visited[start] = True
                for e in graph[start]:
                    dfs_util(e,graph,visited,result)
        visited = defaultdict(bool)
        #result.append(s)
        #visited[s]=True
        for e in self.graph.keys():
            if not visited[e]:
                temp = []
                dfs_util(e,self.graph,visited,temp)
                result.append(temp)

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

    def findShortestPathBFS(self, source, dest, ifPrint=False):
        path = [source]
        pathQueue = [path]
        while len(pathQueue) > 0:
            if ifPrint:
                print pathQueue
            lastPath = pathQueue.pop(0)
            lastNode = lastPath[-1]
            if lastNode == dest:
                return lastPath
            for n in [k for k in self.graph[lastNode] if k not in lastPath]:
                pathQueue.append(lastPath + [n])
        return None
            

if __name__ == '__main__':
    g = Graph()
    g.addEdge(Node('a'),Node('b'))
    g.addEdge(Node('a'),Node('c'))
    g.addEdge(Node('b'),Node('c'))
    g.addEdge(Node('b'),Node('d'))
    g.addEdge(Node('b'),Node('e'))
    g.addEdge(Node('d'),Node('f'))
    g.addEdge(Node('p'),Node('q'))
    result = []
    g.dfs(Node('a'), result)
    print result
    result = []
    g.bfs(Node('a'),result)
    print result
    print g.findShortestPathDFS(Node('a'), Node('f'))
    print g.findShortestPathBFS(Node('a'), Node('f'))

