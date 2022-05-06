#!/usr/bin/python
def findMatches(string, text):
    sizeOfText = len(text)
    mod = 2** 31
    multiplier = 2
    textHash = 0
    for idx in range(len(text)):
        c = text[idx]
        textHash = textHash +  hash(c) * multiplier ** (sizeOfText - idx - 1)
    textHash %= mod
    stringHash = 0
    for idx in range(len(string)):
        inComingChar = string[idx]
        outGoingChar = string[idx - sizeOfText] if idx - sizeOfText >= 0 else None
        if outGoingChar is None:
            stringHash = stringHash +  hash(inComingChar) * multiplier ** (sizeOfText - idx - 1)
        else:
            effectiveHashOfGoingChar = hash(outGoingChar) * multiplier ** (sizeOfText -1)
            stringHash = (stringHash - effectiveHashOfGoingChar) * multiplier + hash(inComingChar)
        if stringHash % mod  == textHash and idx >= sizeOfText -1:
            match = True
            for i in range(sizeOfText):
                textChar = text[i]
                patternChar = string[idx - sizeOfText + 1 + i]
                if textChar == patternChar:
                    continue
                else:
                    match = False
                    break
            if match == True:
                print (f'Match found at index {idx - sizeOfText + 1}')


if __name__ == '__main__':
    ex_text = 'bacbabababcaabcbabbacbabababcaabcbab'
    ex_pattern = 'abababca'
    findMatches(ex_text, ex_pattern)
