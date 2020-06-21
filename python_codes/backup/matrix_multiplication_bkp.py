#!/usr/bin/python
import sys
import numpy as np
def find_optimum_parenthesis(n,p,m,s):
    for l in range(1,n):
        for i in range(1,n-l+1):
            j=i+l
            m[i-1][j-1]=sys.maxint
            for k in range(i,j):
                q=m[i-1][k-1]+m[k][j-1]+p[i-1]*p[k]*p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1]=q
                    s[i-1][j-1]=k

def print_solution(n,s,solution):
    def print_solution_util(s,i,j,solution):
        if i == j:
            solution.extend(' matrix{i} '.format(i=i))
        else:
            solution.extend('(')
            print_solution_util(s,i,s[i-1][j-1],solution)
            #print ')',
            #print '(',
            print_solution_util(s,s[i-1][j-1]+1,j,solution)
            solution.extend(')')
    print_solution_util(s,1,n,solution)        

if __name__ == '__main__':
    p=[30,35,15,5,10,20,25]
    size = len(p) -1
    m = [[0]*size  for _ in range(size)]
    s = [[0]*size for _ in range(size)]
    find_optimum_parenthesis(size, p,m,s)
    print "optimum cost matrix cost_matrix:\n {cost} ".format(cost=np.matrix(m))
    print "optimum cost matrix solution_matrix:\n {sol} ".format(sol=np.matrix(s))
    solution=[] 
    print_solution(size,s,solution)
    print ''.join(solution)
