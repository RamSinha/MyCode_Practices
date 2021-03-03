#!/usr/bin/python

def solution(A):
    sorted_list = sorted(A)
    mid= sorted_list[len(sorted_list)/2 -1]
    increasing = []
    decreasing = []

    if len(sorted_list) >2:
        increasing.append(mid)

    #print 'sort = {mid}'.format(mid=sorted_list)
    #print 'input = {mid}'.format(mid=A)
    #print 'mid = {mid}'.format(mid=mid)
    for i in sorted_list:
        if i > mid:
            if not increasing:
                increasing.append(i)
                #print 'increasing = {increasing}'.format(increasing=increasing)
            elif increasing[-1] != i:
                increasing.append(i)
                #print 'increasing = {increasing}'.format(increasing=increasing)
        else:
            if not decreasing:
                decreasing = [i] + decreasing
                #print 'decreasing = {decreasing}'.format(decreasing=decreasing)
            elif decreasing[0] != i:
                decreasing = [i] + decreasing
                #print 'decreasing = {decreasing}'.format(decreasing=decreasing)
    print (increasing + decreasing)


if __name__ == '__main__':
    solution([2,5,3,2,4,1])
    solution([1,2])
    solution([2,3,3,2,2,2,1])
