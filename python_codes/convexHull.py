#!/usr/bin/python


'''
cross product of two vector gives SIGNED area of the parallelogram created
if W is counter clockwise to V then V x W -> positive
if W is clockwise to V then V x W -> negative
'''


def ccw (a, b, c):
    area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if area < 0:
        return -1 # clockwise
    if area > 0:
        return 1 # counter clockwise

    else:
        return 0 # collinear

