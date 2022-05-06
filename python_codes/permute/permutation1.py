#!/usr/bin/python

def permute(string):
    # base case
    if len(string) <= 1:
        return [string]

    lastChar = string[-1]
    temp = string[:len(string)-1]
    partialPermutations = permute(temp)
    result = []
    for partialPermutation in partialPermutations:
        for idx in range(len(partialPermutation) + 1):
            result.append(partialPermutation[:idx] + lastChar + partialPermutation[idx:])
    return result        

if __name__ == '__main__':
    print (permute('ab'))
    print (permute('abc'))
