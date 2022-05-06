#!/usr/bin/python

def isUnique(string):
    freq = {}
    for c in string:
        if c in freq:
            return False
        else:
            freq[c] = True
    return True



#without extra space:
def isUniqueWithoutSpace(string):
    string.sort()
    for idx in range(1, len(string)):
        if string[idx] == string[idx-1]:
            return False
    return True    


def isUniqueWithLimitedChars(string):
    bitVector = 0
    for c in string:
        idx = ord(c) - 97
        if (bitVector & 1 << idx):
            return False
        else:
            bitVector |= 1 << idx
    return True




if __name__ == '__main__':
    assert(isUnique('abcd') == True)
    assert(isUnique('abca') == False)
    assert(isUnique('') == True)
    assert(isUniqueWithoutSpace(list('abcd')) == True)
    assert(isUniqueWithoutSpace(list('abca')) == False)
    assert(isUniqueWithoutSpace(list('')) == True)
    assert(isUniqueWithLimitedChars(list('abcd')) == True)
    assert(isUniqueWithLimitedChars(list('abca')) == False)
    assert(isUniqueWithLimitedChars(list('')) == True)
