import sys

global N

def find_start(jungle):
    i=0
    j=0
    for row in jungle:
        j=0
        for column in row:
            if (column=='S'):
                return (i,j)
            j+=1
        i+=1

def is_visited(x,y,jungle):
    if 0<=x<N and  0<=y<N and jungle[x][y]=='V':
        return True
    else:
        return False

def find_destination(jungle):
    i=0
    j=0
    for row in jungle:
        j=0
        for column in row:
            if (column=='S'):
                return (i,j)
            j+=1
        i+=1

def get_min(values):
    minimum = sys.maxint
    for i in values:
        if i is not None and i < minimum:
            minimum=i
    return minimum
        

def is_safe(x,y,jungle):
    if 0<=x<N and  0<=y<N and jungle[x][y]!='T':
        return True
    else:
        return False


def is_dest(x,y,jungle):
    if 0<=x<N and  0<=y<N and jungle[x][y]=='E':
        return True
    else:
        return False

def get_min_step(jungle, x, y, steps):
   
    if is_dest(x,y,jungle):
        return steps
    if is_visited(x,y,jungle):
        return None

    k1=None
    k2=None
    k3=None
    k4=None
    if is_safe(x,y,jungle) == True:
        
        current=jungle[x][y]
        jungle[x][y]='V'
        k1 = get_min_step(jungle, x+1, y, steps+1)
        k2 = get_min_step(jungle, x-1, y, steps+1)
        k3 = get_min_step(jungle, x, y+1, steps+1)
        k4 = get_min_step(jungle, x, y-1, steps+1)
        jungle[x][y]=current

        return get_min([k1,k2,k3,k4])
    else:
        return sys.maxint


if __name__=='__main__':
   global N
   no_of_line = int(raw_input().strip())
   N = no_of_line
   jungle=[[value for value in raw_input().strip().split()] for x in range(no_of_line)]
   (x,y) = find_start(jungle)
   print get_min_step(jungle,x,y,0)
    


