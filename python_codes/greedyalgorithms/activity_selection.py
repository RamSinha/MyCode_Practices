#!/usr/bin/python
import sys
from operator import itemgetter

def findMaxActivitiesIterative(pair):
    result = []
    for i in range(0, len(pair)):
        if result:
            last = result[-1]
            if pair[i][0] >= pair[last][1]:
                result.append(i)
        else:
            result.append(i)
    return map(lambda x: 'a{x}'.format(x=x+1), result)


def findMaxActivities(pair):
    def findMaxActivitiesUtil(pair, index, last, result):
        k = -1
        for i in range(index, len(pair)):
            if pair[i][0] < pair[last][1]:
                continue
            else:
                k = i
                break
        if k > -1:
            result.append('a{i}'.format(i=i+1))
            findMaxActivitiesUtil(pair, k+1, k, result)
    if not pair:
        return []
    result = ['a{i}'.format(i=1)]
    findMaxActivitiesUtil(pair, 1, 0, result)
    return result

if __name__ == '__main__':
    activity_start = map(lambda x : int(x), raw_input('enter start of activities ex: 1,3,0,5,3,5,6,8,8,2,12\n').split(","))
    activity_end = map(lambda x : int(x), raw_input('enter end of activities ex: 4,5,6,7,9,9,10,11,12,14,16\n').split(","))
    assert (len(activity_start) == len(activity_end))
    pair = zip(activity_start, activity_end)
    pair.sort(key=itemgetter(1))
    print findMaxActivitiesIterative(pair)
    print findMaxActivities(pair)
