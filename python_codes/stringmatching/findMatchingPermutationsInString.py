#!/usr/bin/python

# O(len(bigger)) | O(len(smaller))
# using sliding window and couting characters
# important trick of using barriar
def findMatchingPermutationsInStringOptimized(small, bigger):
    charFreqTableSmall = {}
    noOfChar = 0
    for c in small:
        if c not in charFreqTableSmall:
            charFreqTableSmall[c] = 0
        charFreqTableSmall[c] += 1
    noOfChar = len(charFreqTableSmall)    
    swl = len(small) # sliding window length
    noc = 0 # number of occurance

    idx = 0
    freq = {}
    mc = 0
    barriar = 0
    while idx < len(bigger):
        inComingChar = bigger[idx]
        if idx - swl >= barriar:
            outGoingChar = bigger[idx - swl]
            if outGoingChar in freq:
                if outGoingChar in charFreqTableSmall:
                    if freq[outGoingChar] == charFreqTableSmall[outGoingChar]:
                        mc -= 1
                freq[outGoingChar] -= 1
        if inComingChar not in charFreqTableSmall:
            freq = {}
            mc = 0
            barriar = idx
            idx += 1
            continue
        if inComingChar not in freq:
            freq[inComingChar] = 0
        freq[inComingChar] += 1
        if freq[inComingChar] == charFreqTableSmall[inComingChar]:
            mc += 1
        if mc == noOfChar:
            noc += 1
        idx += 1
    return noc

def findMatchingPermutationsInString(small, bigger):
    charFreqTableSmall = {}
    for c in small:
        if c not in charFreqTableSmall:
            charFreqTableSmall[c] = 0
        charFreqTableSmall[c] += 1
    swl = len(small) # sliding window length
    noc = 0 # number of occurance

    idx = 0
    while idx + swl <= len(bigger):
        bidx = idx
        freq = {}
        for sidx in range(swl):
            bChar = bigger[bidx]
            if bChar not in freq:
                freq[bChar] = 0
            freq[bChar] += 1    
            if bChar in charFreqTableSmall and freq[bChar] <= charFreqTableSmall[bChar]:
                bidx += 1
            else:
                break
        if bidx - idx == swl:
            noc += 1
        idx += 1
    return noc

if __name__ == '__main__':
    smaller = 'abc'
    bigger = 'abcxavcbac'
    print (findMatchingPermutationsInString(smaller, bigger))

    smaller = 'abbc'
    bigger = 'cbabadcbbabbcbabaabccbabc'
    print (findMatchingPermutationsInString(smaller, bigger))

    print (findMatchingPermutationsInString('a', ''))
    smaller = 'abc'
    bigger = 'abcxavcbac'
    print (findMatchingPermutationsInStringOptimized(smaller, bigger))

    smaller = 'abbc'
    bigger = 'cbabadcbbabbcbabaabccbabc'
    print (findMatchingPermutationsInStringOptimized(smaller, bigger))

    print (findMatchingPermutationsInStringOptimized('a', ''))



