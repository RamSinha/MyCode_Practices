#!/usr/bin/python

import sys
from operator import itemgetter
import numpy as np

'''
ex: W = 100
assume there are 100 buckets each with capacity 1,2,3,4,... 100
Now the algo try to check first 
1- how much value can we generate using 1st item (assuming we have 100 buckets)
2- how much value can we generate using 1st and 2nd item (assuming we have 100 buckets)
3- how much value can we generate using 1st and 2nd and 3rd item (assuming we have 100 buckets)
.
.
.
n- how much value can we generate using 1st and 2nd and 3rd ... nth item (assuming we have 100 buckets)
return c[n][w] => This is the maximum value that can be generated.
'''
def fillKnapSack(price, weight, W):
    pair = zip(price,weight) 
    sol = [[-sys.maxint-1]*(W+1) for _ in range(len(pair)+1)]
    for i in range(0,W+1):
        sol[0][i]=0 #total generated value when there is no item to choose is zero
    for j in range(0, len(pair)+1):
        sol[j][0] = 0 #total generated value when there is no bucket is zero
    for i in range(1,len(pair)+1):
        for j in range(1,W+1):
            if pair[i-1][1] > j:
                sol[i][j] = sol[i-1][j]
            else:
                sol[i][j] = max(sol[i-1][j], sol[i-1][j-pair[i-1][1]] + pair[i-1][0])
    #print np.matrix(sol)
    return sol[len(pair)][W]

if __name__ == '__main__':
    price = map(lambda x : int(x), raw_input('enter the price list ex: 60,100,120 \n').split(','))
    weight = map(lambda x : int(x), raw_input('enter the weight list ex: 10,20,30 \n').split(','))
    capacity = int(raw_input('Enter maximum knapsack capacity\n'))
    assert(len(price) == len(weight))
    #print 'price is {price}'.format(price=price)
    #print 'weight is {weight}'.format(weight=weight)
    #print 'capacity is {capacity}'.format(capacity=capacity)
    print 'Maximum profit = {profit}'.format(profit = fillKnapSack(price, weight, capacity))


