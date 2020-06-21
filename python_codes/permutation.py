#!/usr/bin/python
def permute(inputStr, d):
    if d == len(inputStr) -1:
        print (inputStr)
    else:
        lastSwap = None
        for i in range(d, len(inputStr)):
            if lastSwap == inputStr[i]:
                continue
            lastSwap = inputStr[i]
            inputStr = swap(inputStr, d, i)
            permute(inputStr, d + 1)
            inputStr = swap(inputStr, d, i)
def swap(s,i,j):
    c = list(s)
    c[i],c[j] = c[j],c[i]
    return ''.join(c)

permute("abcd",0)
