#!/usr/bin/python
import numpy as np

def activity_selection_problem(array):
    dummyStartActivity = [(0,0)]
    dummyEndActivity = [(max(map(lambda x : x[1], array)) + 1 ,float('inf'))]
    array = dummyStartActivity + array + dummyEndActivity # Two entries are added
    n = len(array)
    c = [[None for _ in range(n)] for _ in range(n)]
    solution = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        c[i][i] = 0

    for i in range(n-1):
        c[i][i+1] = 0

    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l -1
            k = j -1
            c[i][j] = 0
            while (k >i and array[i][1] < array[k][1]):
                #take only those activity whose start time is more than i's finish 
                #and finish time is less than j's start
                #print('i ={}, k={}, j={}'.format(i,k,j))
                # finish time of i array[i][1]
                # start time of k array[k][0]
                # start time of j array[j][0]
                # finish time of k array[k][1]
                if array[i][1] <= array[k][0] and array[k][1] <= array[j][0] and 1 + c[i][k] + c[k][j] > c[i][j]:
                    c[i][j] = c[i][k] + c[k][j] + 1
                    solution[i][j] = k
                k -= 1
                #print('i ={}, k ={}'.format(i,k))
    #print (np.matrix(c))    
    #print (np.matrix(solution))
    printOptimalSchedule(solution, 0, n-1)

def printOptimalSchedule(sol, i, j):
    if not sol[i][j]:
        return
    printOptimalSchedule(sol, i, sol[i][j])
    print 'a{} '.format(sol[i][j]) ,
    printOptimalSchedule(sol, sol[i][j], j)


if __name__ == '__main__':
    activity_start = [1,3,0,5,3,5,6,8,8,2,12]
    activity_end = [4,5,6,7,9,9,10,11,12,14,16]
    assert (len(activity_start) == len(activity_end))
    pair = zip(activity_start, activity_end)
    pair.sort(key=lambda x: x[1])
    activity_selection_problem(pair)
    #print findMaxActivitiesIterative(pair)
    #print findMaxActivities(pair)
