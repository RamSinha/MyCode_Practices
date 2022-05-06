#!/usr/bin/python

def kPermuteNoRepeat(charList, k, prefix):
    if k==0:
        print prefix
    else:
        for idx in range(len(charList)):
            temp = prefix + charList[idx]
            kPermute(charList[0:idx] + charList[idx+1:], k-1, temp)


def kPermute(charList, k, prefix):
    if k==0:
        print prefix
    else:
        for idx in range(len(charList)):
            temp = prefix + charList[idx]
            kPermute(charList, k-1, temp)

if __name__ == '__main__':
    s = ['a', 'b', 'c']
    kPermute(s, 2, "")
    #kPermuteNoRepeat(s, 2, "")
