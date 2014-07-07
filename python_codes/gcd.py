def fun(a,b):
    if a == 0:
        return b
    if a > b:
       return fun(a%b,b)
    return fun(b%a,a)

def hcf(a,b):
    print (a*b)/fun(a,b)

if __name__ == '__main__':
    l = raw_input().strip().split(' ')
    hcf(int(l[0]), int(l[1]))

