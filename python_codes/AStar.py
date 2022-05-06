def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
	startNode = nodes[startRow][startCol]
	endNode = nodes[endRow][endCol]
	
	
	startNode.distanceFromStart = 0
	startNode.estimatedDistanceToEnd = manhattanDistance(startNode, endNode)
	
	nodeToVisit = MinHeap()
	nodeToVisit.insert(startNode)
	
	while not nodeToVisit.isEmpty():
		bestOption = nodeToVisit.remove(0)
		
		if bestOption == endNode:
			break
		
		for n in getNeighboringNodes(bestOption, nodes):
			if n.value == 1:
				continue
				
			tentativeDistanceFromStart = 1 + bestOption.distanceFromStart
			
			if tentativeDistanceFromStart >= n.distanceFromStart:
				continue
			
			n.cameFrom = bestOption
			n.distanceFromStart = tentativeDistanceFromStart
			n.estimatedDistanceToEnd = tentativeDistanceFromStart + manhattanDistance(n, endNode)
			
			if nodeToVisit.contains(n):
				nodeToVisit.update(n)
			else:
				nodeToVisit.insert(n)
				
	return constructPath(endNode)
	
def constructPath(endNode):
	if endNode.cameFrom is None:
		return []
	
	path = []
	
	while endNode:
		path.append([endNode.row, endNode.col])
		endNode = endNode.cameFrom
	return path[::-1]
	


def getNeighboringNodes(node, nodes):
	rows = len(nodes)
	cols = len(nodes[0])
	neighbors = []
	r = node.row
	c = node.col
	
	if r + 1  < rows:
		neighbors.append(nodes[r+1][c])
	if r - 1  >= 0:
		neighbors.append(nodes[r-1][c])
	if c + 1  < cols:
		neighbors.append(nodes[r][c+1])
	if c - 1  >= 0:
		neighbors.append(nodes[r][c -1])
	return 	neighbors
		
def initializeNodes(graph):
	nodes = [[None for _ in x] for x in graph]
	for rowIdx, rows in enumerate (graph):
		for colIdx, val in enumerate(rows):
			nodes[rowIdx][colIdx] = Node(rowIdx, colIdx, val)
	return nodes		

def manhattanDistance(currentNode, endNode):
	startRow, startCol, endRow, endCol = currentNode.row, currentNode.col, endNode.row, endNode.col
	return abs(startRow - endRow) + abs(startCol - endCol)

class Node:
	def __init__(self, row, col, value):
		self.id = str(row) + "_" + str(col)
		self.row = row
		self.col = col
		self.value = value # F 
		self.distanceFromStart = float('inf') # G
		self.estimatedDistanceToEnd = float('inf') # H
		self.cameFrom = None
		
class MinHeap:
	def __init__(self):
		self.elements = []
		self.nodeToIdx = {}
		
	
	def insert(self, node):
		self.elements.append(node)
		self.nodeToIdx[node.id] = len(self.elements) -1
		self.siftUp(self.nodeToIdx[node.id], node)
		
	def siftUp(self, childIdx, node):
		parentIdx = (childIdx - 1) // 2 
		while parentIdx >= 0 and self.elements[parentIdx].estimatedDistanceToEnd > self.elements[childIdx].estimatedDistanceToEnd:
			self.swap (parentIdx, childIdx)
			childIdx = parentIdx
			parentIdx = (childIdx - 1) // 2
			
	def siftDown(self, idx):
		parentIdx = idx
		leftChildIdx = idx * 2 + 1 
		rightChildIdx = idx * 2 + 2 
		size = len(self.elements)
		minIdx = parentIdx
		if leftChildIdx < size and self.elements[leftChildIdx].estimatedDistanceToEnd < self.elements[parentIdx].estimatedDistanceToEnd:
			minIdx = leftChildIdx
		if rightChildIdx < size and self.elements[rightChildIdx].estimatedDistanceToEnd < self.elements[minIdx].estimatedDistanceToEnd:
			minIdx = rightChildIdx
		if minIdx != parentIdx:
			self.swap(minIdx, parentIdx)
			self.siftDown(minIdx)
			
	
	def remove(self, index):
		self.swap(index, len(self.elements) -1)
		root = self.elements.pop()
		del self.nodeToIdx[root.id]
		self.siftDown(0)
	    return root
	
	def update(self, node):
		self.siftUp(self.nodeToIdx[node.id], node)
	
	def swap(self, i, j):
		# swap the indexes as well
		self.nodeToIdx[self.elements[i].id], self.nodeToIdx[self.elements[j].id] = self.nodeToIdx[self.elements[j].id], self.nodeToIdx[self.elements[i].id]
		# swap the elements
		self.elements[i] , self.elements[j] = self.elements[j] , self.elements[i]
	
	def contains(self, node):
		return node.id in self.nodeToIdx
	
	def isEmpty(self):
		return len(self.elements) == 0
		