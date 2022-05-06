#!/usr/bin/python
def rejections(series, t = 0):
    rejectionCounts = 0
    for c in series:
        if t != 0:
            t -=1
        if c == 'N':
            continue
        if c == 'C':
            if t == 0:
                t = 3
            else:
                rejectionCounts += 1
    return rejectionCounts            

print (rejections(['C', 'N', 'C', 'C', 'N', 'N', 'N', 'N', 'C', 'C', 'N', 'C']))
