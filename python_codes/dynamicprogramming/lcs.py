#!/usr/bin/python
import sys
import numpy as nm

def find_longest_common_subsequence(first, second, c, s):
    for i in range(0,len(first)):
        for j in range(0,len(second)):
            if first[i]==second[j]:
                s[i][j] = 'centre'
                if i>0 and j>0:
                    c[i][j]=c[i-1][j-1]+1
                else:
                    c[i][j]=1
            else:
                if i>0 and j>0:
                    if c[i-1][j] > c[i][j-1]:
                        c[i][j]=c[i-1][j]
                        s[i][j]='up'
                    else:
                        c[i][j]=c[i][j-1]
                        s[i][j]='left'
                elif i>0:
                    c[i][j]=c[i-1][j]
                    s[i][j]='up'
                elif j>0:
                    c[i][j]=c[i][j-1]
                    s[i][j]='left'
                elif i==0 and j==0:
                    c[i][j]=0
                    s[i][j]='left'

#exercise 15.4-2

def print_lcs_with_length_metrics_only(s1,s2,c,solution):
    def print_lcs_with_length_metrics_only_util(s1,s2,i,j,c,solution):
        if i == 0 or j == 0:
            if c[i][j] > 0:
                solution.append(s1[i])
        else:        
            if c[i][j] == c[i-1][j]:
                print_lcs_with_length_metrics_only_util(s1,s2,i-1,j,c,solution)
            elif c[i][j] == c[i][j-1]:
                print_lcs_with_length_metrics_only_util(s1,s2,i,j-1,c,solution)
            else:
                print_lcs_with_length_metrics_only_util(s1,s2,i-1,j-1,c,solution)
                solution.append(s1[i])

    print_lcs_with_length_metrics_only_util(s1,s2,len(s1)-1,len(s2)-1,c,solution)

'''
#exercise 15.4-2
def print_lcs_with_length_metrics_onlyi_test(s1,s2,c,solution):
    def print_lcs_with_length_metrics_only_util(s1,s2,i,j,c,solution):
        if i == 0 and j == 0:
            if c[i][j] > 0:
                solution.appen(s1[i])
        else:        
            if i>0 and j>0 and c[i][j] > c[i-1][j] and c[i][j] > c[i][j-1]:
                print_lcs_with_length_metrics_only_util(s1,s2,i-1,j-1,c,solution)
                solution.append(s1[i])
            if i > 0 and j == 0 and c[i][j] > c[i-1][j]:
                print_lcs_with_length_metrics_only_util(s1,s2,i-1,j-1,c,solution)
                solution.append(s1[i])
            if i == 0 and j > 0 and c[i][j] > c[i][j-1]:
                print_lcs_with_length_metrics_only_util(s1,s2,i-1,j-1,c,solution)
                solution.append(s1[i])
            else:
                if i > 0 and c[i][j] == c[i-1][j]:
                    print_lcs_with_length_metrics_only_util(s1,s2,i-1,j,c,solution)
                elif j > 0 and c[i][j] == c[i][j-1]:
                    print_lcs_with_length_metrics_only_util(s1,s2,i,j-1,c,solution)
    print_lcs_with_length_metrics_only_util(s1,s2,len(s1)-1,len(s2)-1,c,solution)
'''

def print_lcs(s1, s2, s, solution):
    def print_lcs_util(s1,s2,s,i,j,solution):
        if i>=0 and j>=0:
            if s[i][j]=='centre':
                print_lcs_util(s1,s2,s,i-1,j-1,solution)
                solution.append(s1[i])
            elif s[i][j]=='left':    
                print_lcs_util(s1,s2,s,i,j-1,solution)
            elif s[i][j]=='up':    
                print_lcs_util(s1,s2,s,i-1,j,solution)
    print_lcs_util(s1,s2,s,len(s1)-1, len(s2)-1,solution)            

def do_test(s1,s2):
    c = [[0]*len(s2) for i in range(len(s1))]
    s = [[0]*len(s2) for i in range(len(s1))]
    find_longest_common_subsequence(s1,s2,c,s)
    solution=[]
    print_lcs(s1,s2,s,solution)
    print "s1={s1}\ns2={s2}\nlcs={lcs}".format(s1=s1, s2=s2, lcs=''.join(solution))
    #print "s1={s1}, s2={s2},\ncost:\n{cost}\nsol:\n{sol}\nlcs= {lcs}".format(s1=s1, s2=s2, cost=nm.matrix(c), sol=nm.matrix(s),lcs=''.join(solution))
    print ("\nMETHOD-2 \n")
    solution=[]
    print_lcs_with_length_metrics_only(s1,s2,c,solution)
    print "s1={s1}\ns2={s2}\nlcs={lcs}".format(s1=s1, s2=s2, lcs=''.join(solution))
    #print "s1={s1}, s2={s2},\ncost:\n{cost}\nsol:\n{sol}\nlcs= {lcs}".format(s1=s1, s2=s2, cost=nm.matrix(c), sol=nm.matrix(s),lcs=''.join(solution))

if __name__ == '__main__':
    #do_test('ab','a')
    #do_test('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA','GTCGTTCGGAATGCCGTTGCTCTGTAAA')
    do_test('ABCBDAB','BDCABA')
    print "\nNEW TEST \n"
    do_test('ABCBAB','BCABA')

