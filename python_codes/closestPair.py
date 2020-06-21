#!/usr/bin/python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return ( (self.x - point.x)**2 + (self.y - point.y)**2 )**0.5

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

def bruteForce(points):
    if len(points) == 2:
        return points[0].distance(points[1])
    if len(points) == 3:
        return min(points[0].distance(points[1]), points[0].distance(points[2]), points[1].distance(points[2]))
    raise Exception('Not valid')
    
def findMin(strip,d):
    minDis = d
    stripSize = len(strip)
    for i in range(stripSize):
        j = i+1
        while(j < stripSize and abs(strip[i].y - strip[j].y) < minDis):
            minDis = min(minDis, strip[i].distance(strip[j]))
            j+=1
    return minDis 
            

def findShortest(points, points_ySorted):
    left = 0
    right = len(points) - 1
    if len(points) <= 3:
        return bruteForce(points[left:right+1])
    mid = right + ( left - right ) / 2 
    dLeft = findShortest(points[left:mid+1], points_ySorted)
    dRight = findShortest(points[mid+1:right+1], points_ySorted)
    strip = [p for p in points_ySorted if abs(p.x - points[mid].x) < min(dLeft, dRight)]
    return findMin(strip, min(dLeft, dRight))


if __name__ == '__main__':
    p = [Point(2, 3), Point(12, 30),
        Point(40, 50), Point(5, 1),
        Point(12, 10), Point(3, 14),
        Point(0,0)]
    print "The smallest distance is {}".format(findShortest(sorted(p, key=lambda x: x.x), sorted(p, key=lambda x: x.y)))



##!/usr/bin/python
#class Point(object):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def distance(self, point):
#        return ( (self.x - point.x)**2 + (self.y - point.y)**2 )**0.5
#
#    def __repr__(self):
#        return "({}, {})".format(self.x, self.y)
#
#def bruteForce(points):
#    if len(points) == 2:
#        return points[0].distance(points[1])
#    if len(points) == 3:
#        return min(points[0].distance(points[1]), points[0].distance(points[2]), points[1].distance(points[2]))
#    raise Exception('Not valid')
#    
#def findMin(strip,d):
#    minDis = d
#    stripSize = len(strip)
#    for i in range(stripSize):
#        j = i+1
#        while(j < stripSize and abs(strip[i].y - strip[j].y) < minDis):
#            minDis = min(minDis, strip[i].distance(strip[j]))
#            j+=1
#    return minDis 
#            
#
#def findShortest(points, points_ySorted):
#    left = 0
#    right = len(points) - 1
#    print "x ->",
#    print points
#    print "y ->",
#    print points_ySorted
#    if len(points) <= 3:
#        return bruteForce(points[left:right+1])
#    mid = right + ( left - right ) / 2 
#    dLeft = findShortest(points[left:mid+1], points_ySorted)
#    print 'dLeft is {}'.format(dLeft)
#    dRight = findShortest(points[mid+1:right+1], points_ySorted)
#    print 'dRight is {}'.format(dRight)
#    strip = [p for p in points_ySorted if abs(p.x - points[mid].x) < min(dLeft, dRight)]
#    print 'strip ->',
#    print strip
#    return findMin(strip, min(dLeft, dRight))
#
#
#if __name__ == '__main__':
#    p = [Point(2, 3), Point(12, 30),
#        Point(40, 50), Point(5, 1),
#        Point(12, 10), Point(3, 14),
#        Point(0,0)]
#    print("The smallest distance is", findShortest(sorted(p, key=lambda x: x.x), sorted(p, key=lambda x: x.y)))



