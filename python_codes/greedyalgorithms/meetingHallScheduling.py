#!/usr/bin/python
from queue import PriorityQueue
def findMinNumberOfMeetingHalls(meetings):
    if not meetings:
        return 0
    q = PriorityQueue()
    meetings.sort(key = lambda x : x[0]) # sort with start time
    for i in range(len(meetings)):
        if q.empty():
            q.put(meetings[i][1])
            continue
        closetMeetingRoom = q.get()
        if meetings[i][0] >= closetMeetingRoom:
            q.put(meetings[i][1])
        else:
            q.put(meetings[i][1])
            q.put(closetMeetingRoom)
    return q.qsize()        

if __name__ == '__main__':
    activity_start = map(lambda x : int(x), raw_input('enter start of activities ex: 1,3,0,5,3,5,6,8,8,2,12\n').split(","))
    activity_end = map(lambda x : int(x), raw_input('enter end of activities ex: 4,5,6,7,9,9,10,11,12,14,16\n').split(","))
    assert (len(activity_start) == len(activity_end))
    pair = zip(activity_start, activity_end)
    print (findMinNumberOfMeetingHalls(pair))
