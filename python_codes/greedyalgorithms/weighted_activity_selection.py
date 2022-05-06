#!/usr/bin/python
from queue import PriorityQueue

def getMaxWeightedCompatibleActivities(activities):
    listOfGroups = [] # put tuples  (q, activities)
    indexLookUp = range(len(activities))
    indexLookUp.sort(key = lambda x : activities[x][1], reverse = False )
    activities.sort(key = lambda x : x[1], reverse = False)
    #print (activities)
    #print (indexLookUp)
    for i in range(len(activities)):
        groupCompatibleGroup = None
        for g in listOfGroups:
            q = g[0]
            activitiesInGroup = g[1]
            top = q.get()
            if activities[i][0] >= top:
                #q.put(top)
                q.put(activities[i][1])
                groupCompatibleGroup = g
                activitiesInGroup.append(i)
                #activitiesInGroup.append('a{i}'.format(i=indexLookUp[i]))
            else:
                q.put(top)
        if not groupCompatibleGroup:
            q = PriorityQueue()
            q.put(activities[i][1])
            activitiesInGroup = [i]
            listOfGroups.append((q,activitiesInGroup))
    maxWeight = -1
    maxGroup = None
    for i in listOfGroups:
        g = i[1]
        groupWeight = sum (map(lambda x : activities[x][2], g))
        if groupWeight > maxWeight:
            maxWeight = groupWeight
            maxGroup = map(lambda x : 'a{idx}'.format(idx=indexLookUp[x]), g)
    print (maxGroup, maxWeight)        

    
if __name__ == '__main__':
    getMaxWeightedCompatibleActivities([(0,9,100), (1,4,80), (2,6,95), (5,7,5), (8,11,10)])

