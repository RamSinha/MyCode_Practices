#!/usr/bin/python

def isPermutation(string1, string2):
    freq = {}
    for c in string1:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1    
    for c in string2:
        if c not in freq:
            return False
        freq[c] -= 1
    for f in freq:
        if freq[f] != 0:
            return False
    return True    


def isPermutationBasedOnOrdinal(string1, string2):
    if len(string1) != len(string2):
        return False
    charFreq = [0 for _ in range(26)]
    for c in string1:
        position = ord(c) - 97
        charFreq[position] += 1
    for c in string2:
        position = ord(c) - 97
        charFreq[position] -= 1
        if charFreq[position] < 0:
            return False
    return True    
            



if __name__ == '__main__':
    assert(isPermutation('abc', 'bca') == True)
    assert(isPermutation('abac', 'bcaa') == True)
    assert(isPermutationBasedOnOrdinal('abac', 'bcaa') == True)
    assert(isPermutationBasedOnOrdinal('abac', 'bcaa') == True)
