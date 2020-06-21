#!/usr/bin/python
import copy
def nchooser(data,r,target=[], output=[]):
    for i in range(len(data)):
        newtarget=copy.copy(target)
        newtarget.append(data[i])
        if len(newtarget) == r:
            output.append(newtarget)
        remainingdata=data[i+1:]
        nchooser(remainingdata,r,newtarget,output)
if __name__ == '__main__':
    output = []
    nchooser([1,2,3],2,[], output)
    print output
    print map(lambda x: sorted(x), output)
