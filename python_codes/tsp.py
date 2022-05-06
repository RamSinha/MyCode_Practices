#!/usr/bin/python
def tsp(distances):
    # assuming person starts with 0th index
    vertixes = [False for _ in len(distances)]
    path = [0]
    cost = float('inf')
    for idx in range(1, len(distances)):
        temp = path
        temp.append(idx)
        cost = min (cost,  + tspUtil(distances, distances[0][idx], temp))
    return cost    

def tspUtil(distances, minSoFar, path):
    if len(path) == len(distances):
        return distances[path[-1][0]]
    
    for idx in range(1, len(distances)):
        temp = path
        if idx in path:
            continue
        minSoFar = distances[path[-1][idx]] + tspUtil(path.append(idx), minSoFar, temp.append(idx))
    return minSoFar            
