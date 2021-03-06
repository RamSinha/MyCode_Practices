#!/usr/bin/python
import sys
import time
def max_revenue(p, size):
    if size == 0:
        return 0
    max_cost = -sys.maxsize -1
    for i in range(0, size):
        max_cost = max(max_cost, p[i] + max_revenue(p, size -(i + 1)))
    return max_cost    

def max_revenue_memoized(p, size, memoized):
    if size == 0:
        return 0
    max_cost = -sys.maxsize -1
    if memoized[size-1]:
        return memoized[size-1]
    for i in range(0, size):
        max_cost = max(max_cost, p[i] + max_revenue_memoized(p, size -(i + 1), memoized))
    memoized[size -1] = max_cost
    return max_cost

def print_solution(size, solution):
    print 'cut the given with at below lengths to generate maximum revenue'
    n = size-1 
    while n >= 0:
        print (solution[n]+1), 
        n = n - solution[n] -1
    print ('')

def max_revenue_bootum_up(p, size):
    bottom_up = [None]*(len(p)+1)
    bottom_up[0]=0
    solution = [None]*(len(p))
    for i in range(0, len(p)):
        q=-sys.maxsize -1
        for j in range(0,i+1):
            old = q
            q = max(q, p[j] + bottom_up[i-j])
            if old < q:
                solution[i]=j
        bottom_up[i+1]=q
    print_solution(size, solution)
    return bottom_up[size]

if __name__ == '__main__':
    cost_metrics = [1,5,8,9,10,17,17,20,24,30]
    print 'enter the cost from metrics ex: {cost_metrics}'.format(cost_metrics = ",".join(map(lambda x: str(x), cost_metrics)))
    cost_metrics = map(lambda x: int(x) , raw_input().split(","))
    print 'enter the size of rod: [max allowed size is {size}]'.format(size = len(cost_metrics))
    rod_size = int(raw_input())
    print time.time()
    print 'Max revenue that can be generated is: {revenue}'.format(revenue = max_revenue(cost_metrics, rod_size))
    print time.time()
    print 'Max revenue that can be generated is: {revenue}'.format(revenue = max_revenue_memoized(cost_metrics, rod_size, [None]*len(cost_metrics)))
    print time.time()
    print 'Max revenue that can be generated is: {revenue}'.format(revenue = max_revenue_bootum_up(cost_metrics, rod_size))
    print time.time()
