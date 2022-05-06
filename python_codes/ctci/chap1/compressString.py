#!/usr/bin/python

def compressString(string):
    if not string:
        return string
    counter = 1
    result = []
    for idx in range(1, len(string)):
        if string[idx] == string[idx-1]:
            counter += 1
            continue
        result.append(string[idx-1])
        result.append(str(counter))
        counter = 1
    result.append(string[-1]) 
    result.append(str(counter))
    return ''.join(result) if len(result) < len(string) else string

if __name__ == '__main__':
    assert(compressString('aabcccccaaa') == 'a2b1c5a3')
    assert(compressString('abc') == 'abc')
