def findFailedBuild(build):
    start = 0
    end = len(build) - 1
    while start < end:
        mid = start +  (end - start ) / 2 
        if build[mid] == False:
            end = mid
        else:
            start = mid + 1 
    return end if (build and not build[end]) else -1

if __name__ == '__main__':
    print ("input [True, True, True, True] and output = %s"%(findFailedBuild([True, True, True, True])))
    print ("input [True, False, False, False] and output = %s"%(findFailedBuild([True, False, False, False])))
    print ("input [False, False, False, False] and output = %s"%(findFailedBuild([False, False, False, False])))
    print ("input [True, True, True, False] and output = %s"%(findFailedBuild([True, True, True, False])))
    print ("input [] and output = %s"%(findFailedBuild([])))

