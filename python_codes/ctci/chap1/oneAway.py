#!/usr/bin/python

def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) >= 2:
        return False
    i, j = 0, 0
    bigger = str1 if len(str1) >= len(str2) else str2
    smaller = str1 if len(str1) < len(str2) else str2
    while True:
        if i < len(bigger) and j < len(smaller):
            if bigger[i] == smaller[j]:
                i += 1
                j += 1
                continue
        # check for deletion or replacement, insertion no needed since inserting in bigger will never match    
        return isSame(bigger, smaller, i+1, j) or isSame(bigger, smaller, i+1, j+1)
    return i == len(bigger) # check for case in smaller = abc and bigger = abcdefgds 
            

def isSame(str1, str2, idx1, idx2):
    len1 = len(str1) -1
    len2 = len(str2) -1
    while len1 >= idx1 and len2 >= idx2:
        if str1[len1] != str2[len2]:
            return False
        len1 -= 1
        len2 -= 1
    return len1 == idx1 -1 and len2 == idx2 -1

if __name__ == '__main__':
    assert(isSame('abca', 'bca', 1, 0)  == True  )
    assert(isSame('abca', 'bca', 1, 0)  == True  )
    assert(isSame('', '', 0, 0)         == True  )
    assert(oneAway('pale', 'ple')       == True  )
    assert(oneAway('pales', 'pale')     == True  )
    assert(oneAway('pale', 'bale')      == True  )
    assert(oneAway('pale', 'bae')       == False )
    assert(oneAway('pale', 'bale')      == True  )
