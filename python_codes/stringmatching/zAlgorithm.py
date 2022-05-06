#!/usr/bin/python

def findMatches(text, pattern):
    combinedText = combinePatternAndText(text, pattern)
    zArray = calculateZValue(combinedText)
    for idx in range(len(zArray)):
        if zArray[idx] == len(pattern):
            print ('Found match at {}'.format(idx - len(pattern) -1))


def combinePatternAndText(text, pattern, specialChar = '$'):
    combined = []
    for c in pattern:
        combined.append(c)
    combined.append(specialChar)
    for c in text:
        combined.append(c)
    return ''.join(combined)

'''
zValue[k] = longest SUBSTRING starting at `k` that is also a PREFIX of the string
'''
def calculateZValue(text):
    zArray = [None for _ in range(len(text))]
    zArray[0] = 0
    left = 0
    right = 0
    for k in range(1, len(text)):
        if k > right:
            # i am outside of ZBox
            left, right = k, k
            while right < len(text) and text[right] == text[right -left]:
                right += 1
            zArray[k] = right - left
            right -= 1
        else:
            # i am inside the ZBox
            # find the index of next char
            referenceIdx = k - left
            # check if value in Z at referenceIdx caused overflow?
            # if so then calculate the zScore at that index using usual method
            if zArray[referenceIdx] >= right - k + 1:
                left = k
                while right < len(text) and text[right] == text[right -left]:
                    right += 1
                zArray[k] = right - left
                right -= 1
            else:
                # not causing overflow
                zArray[k] = zArray[referenceIdx]
    return zArray            



if __name__ == '__main__':
    #print (calculateZValue('abcxtpabcxd'))
    text = raw_input('Enter text: ')
    pattern = raw_input('Enter pattern: ')
    findMatches(text, pattern)
    #findMatches('abcxtpabcxd', 'abcxt')
