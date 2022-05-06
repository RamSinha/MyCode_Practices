#!/usr/bin/python

def isPalindromicPermutation(string):
    freqLookup = {}
    totalOddCount = 0
    for c in string:
        if c not in freqLookup:
            freqLookup[c] = 0
        freqLookup[c] += 1
        if freqLookup[c] % 2 == 1:
            totalOddCount += 1
        else:
            totalOddCount -= 1
    return totalOddCount <= 1        


def isPalindromicPermutationUsingBitVector(string):
    vector = 0
    for c in string:
        idx = ord(c) - 97
        vector = toggle(vector, idx)
    return vector == 0 or vector & (vector -1) == 0
    
    

def toggle(vector, idx):
    mask = 1 << idx
    if vector & mask == 0:
        vector |= mask
    else:
        vector &= ~mask
    return vector    

if __name__ == '__main__':
    assert(isPalindromicPermutation('tactcoa') == True)
    assert(isPalindromicPermutation('tactcooa') == True)
    assert(isPalindromicPermutation('tactcooaa') == True)
    assert(isPalindromicPermutation('tactcoooaaaa') == False)
    assert(isPalindromicPermutationUsingBitVector('tactcoa') == True)
    assert(isPalindromicPermutationUsingBitVector('tactcooa') == True)
    assert(isPalindromicPermutationUsingBitVector('tactcooaa') == True)
    assert(isPalindromicPermutationUsingBitVector('tactcoooaaaa') == False)
