#!/usr/bin/python

def urlify(string, l):
    # "Mr Jhom Smith    " # 13
    # output: 'Mr%20Jhom%20Smith'
    s = list(string)
    endIdx = len(s) - 1
    for backwardIdx in range(l)[::-1]:
        if s[backwardIdx] != ' ':
            s[endIdx] = s[backwardIdx]
            endIdx -=1 
            continue
        s[endIdx] = '0'
        s[endIdx-1] = '2'
        s[endIdx-2] = '%'
        endIdx -= 3
    return ''.join(s)

if __name__ == '__main__':
   assert( urlify('Mr Jhon Smith    ', 13) == 'Mr%20Jhon%20Smith')


