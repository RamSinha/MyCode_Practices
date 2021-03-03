#!/usr/bin/python
import sys
import numpy as np

def find_optimum_parenthesis_recursively(n,p,m,s):
    def util(size, dim, cost, sol, start , end):
        if cost[start][end] != None :
            return cost[start][end]
        for k in range(start, end):
            q = util(size, dim, cost, sol, start, k) \
                    + util(size, dim, cost, sol, k+1, end) \
                    + dim[start] * dim[k+1] * dim[end+1]
            if q < cost[start][end] or cost[start][end] == None:
                cost[start][end] = q
                s[start][end] = k
        return cost[start][end]

    k = [[None]*size  for _ in range(size)]
    for i in range(size):
        k[i][i] = 0
    util(n,p,k,s,0,n-1)
    m = k
    print (np.matrix(m))

'''
This methos better way of  handling of positional arguments
'''
def find_optimum_parenthesis_1(n,p,m,s):
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            #print "i={i} and j={j} l={l}".format(i=i, j=j, l=l)
            m[i][j]=float('inf')
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j]=q
                    s[i][j]=k

def find_optimum_parenthesis(n,p,m,s):
    for l in range(1,n):
        for i in range(0,n-l):
            j=i+l
            #print "i={i} and j={j} l={l}".format(i=i, j=j, l=l)
            m[i][j]=sys.maxint
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j]=q
                    s[i][j]=k

def print_solution(n,s,solution):
    def print_solution_util(s,i,j,solution):
        if i == j:
            solution.extend(' matrix{i} '.format(i=i))
        else:
            solution.extend('(')
            print_solution_util(s,i,s[i][j],solution)
            solution.extend(' * ')
            print_solution_util(s,s[i][j]+1,j,solution)
            solution.extend(')')
    print_solution_util(s,0,n-1,solution)

if __name__ == '__main__':
    p=[30,35,15,5,10,20,25]
    #p=[5,10,3,12,5,50,6] exercise: 15.2-1
    size = len(p) -1
    m = [[0]*size  for _ in range(size)]
    s = [[0]*size for _ in range(size)]
    #find_optimum_parenthesis_recursively(size, p,m,s)
    find_optimum_parenthesis_1(size, p,m,s)
    print "optimum cost matrix cost_matrix:\n {cost} ".format(cost=np.matrix(m))
    print "optimum cost matrix solution_matrix:\n {sol} ".format(sol=np.matrix(s))
    #p=[30,35,15,5,10,20,25]
    ##p=[5,10,3,12,5,50,6] exercise: 15.2-1
    #size = len(p) -1
    #m = [[0]*size  for _ in range(size)]
    #s = [[0]*size for _ in range(size)]
    #find_optimum_parenthesis(size, p,m,s)
    #print "optimum cost matrix cost_matrix:\n {cost} ".format(cost=np.matrix(m))
    #print "optimum cost matrix solution_matrix:\n {sol} ".format(sol=np.matrix(s))
    #solution=[] 
    #print_solution(size,s,solution)
    #print ''.join(solution)
