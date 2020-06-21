#!/usr/bin/python
from operator import itemgetter
def generateBestSchedule(acts):
    sortedActs = sorted(acts, key = itemgetter(2), reverse = True)
    if not sortedActs:
        print []
        return
    maxDelay = max(map(lambda x: x[1], sortedActs))
    lookup = [0 for _ in range(maxDelay+1)]
    selected = []
    rejected = []
    for act in sortedActs:
        if act[1] > lookup[act[1]]:
            lookup[act[1]] = 1+lookup[act[1]]
            totalActs = 0
            isRejected = False
            for i,k in enumerate(lookup):
                totalActs = totalActs + k
                if totalActs > i:
                    lookup[act[1]] = lookup[act[1]] -1
                    rejected.append(act)
                    isRejected = True
                    break
            if not isRejected:
                selected.append(act)
        else:
            rejected.append(act)

    #print selected
    #print rejected
    print 'schedule is {}'.format(map(lambda x: x[0], sorted(selected, key=itemgetter(1))) + map(lambda x: x[0], rejected))        
    print 'total penality {}'.format(sum(map(lambda x: x[2], rejected)))


if __name__ == '__main__':
    activity = raw_input('Enter comman separated name of the activity ex: a1,a2,a3,a4,a5,a6,a7\n').split(',')
    deadline = map(lambda x: int(x), raw_input('Enter activity deadlines: 4,2,4,3,1,4,6\n').split(','))
    penality = map(lambda x: int(x), raw_input('Enter activity penalities: 70,60,50,40,30,20,10\n').split(','))
    assert (len(activity) == len(deadline) and len(deadline) == len(penality))
    acts = zip(activity,deadline,penality)
    generateBestSchedule(acts)
