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
    bottom_up = [None]*(len(p))
    bottom_up[0]=p[0]
    solution = [None]*(len(p))
    solution[0]=0
    # no of subproblems -> n
    for i in range(1, len(p)):
        q=-sys.maxsize -1
        # no of choices for each sub-problem -> n
        for j in range(0,i+1):
            old = q
            if i == j:
                q = max(q, p[i])
            else:
                q = max(q, p[j] + bottom_up[i-j-1])
            if old < q:
                solution[i]=j
        bottom_up[i]=q
    print_solution(size, solution)
    print bottom_up
    return bottom_up[size-1]


def max_revenue_memoized_t(p, size, memoized):
    if size == 0:
        return 0
    if memoized[size] and memoized[size]  >= 0:
        return memoized[size]
    q = memoized[size]
    for i in range(1, size+1):
        q = max(q, p[i] + max_revenue_memoized_t(p, size -i , memoized))
    memoized[size] = q
    return q

'''
Below method adds a dummy entry to the input to avoid the positional argument more cohrent with the logic and makes the code more readable
'''
def max_revenue_bootum_up_t(p, size):
    revenue = [None]*(size + 1)
    revenue[0] = 0
    sol = [0]*(size+1)
    for i in range(1, size + 1):
        q=-1
        for j in range(1, i+1):
            newCost = p[j] + revenue[i-j]
            if q < newCost:
                q = newCost
                sol[i] = j
        revenue[i] = q
    def printSol(soln, size):
        if size == 0:
            return ['']
        return [str(soln[size])] + printSol(soln, size - soln[size])
    print('Optimal cuts for size= ' + str(size) +  ' are as follows [' + ' '.join(printSol(sol, size)).strip() + '] with max revenue = '+ str(revenue[size]))
    return revenue[size]    

if __name__ == '__main__':
    #cost_metrics = [1,5,8,9,10,17,17,20,24,30]
    #print (max_revenue_bootum_up_t([0]+cost_metrics , 4))
    #print (max_revenue_bootum_up_t([0]+cost_metrics , 6))
    #print (max_revenue_bootum_up_t([0]+cost_metrics , 7))
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
    print 'Max revenue that can be generated is: {revenue}'.format(revenue = max_revenue_memoized_t([0] + cost_metrics, rod_size, [None]*(rod_size+1)))
    print time.time()
