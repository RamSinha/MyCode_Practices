#!/usr/bin/python

def m_search(a, p):
    if not a:
        return -1
    start = 0 
    end = len(a) -1
    while start <= end:
        mid = start + (end - start) / 2
        if a[mid] == p:
            return mid
        if a[mid] < p:
            start = mid + 1
        else:
            end = mid - 1 
    return -1        

def search(a, p):
    if not a:
        return -1
    start = 0 
    end = len(a) -1
    while start < end -1:
        mid = start + (end - start) / 2
        #print mid
        if a[mid] <= p:
            start = mid
        else:
            end = mid 
    return end

if __name__ == '__main__':
    print search([1,3,5,7,11,13,19,21], 11)
    print search([1,3,5,7,11,13,19,21], 13)
    print search([1,3,5,7,11,13,19,21], 1)
    print search([1,3,5,7,11,13,19,21], 19)
    print search([1,3,5,7,11,13,19,21], 21)
    print search([1,3,5,7,11,13,19,21], 211)
    print search([3,5], 2)
