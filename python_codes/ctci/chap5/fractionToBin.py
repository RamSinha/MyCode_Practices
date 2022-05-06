#!/usr/bin/python
def fractionToBin(dec):
    result = []
    while dec > 0:
        if len(result) >= 32:
            raise Exception('Invalid input')
        else:
            dec = 2 * dec
            if dec >= 1:
                result.append('1')
                dec = dec - 1
            else:
                result.append('0')
    return ''.join(result[::-1])


def fractionToBin2(dec):
    frac = 0.5
    result = []
    while dec > 0:
        if len(result) >= 32:
            raise Exception('Invalid input')
        else:
            if dec >= frac:
                result.append('1')
                dec = dec - frac
            else:
                result.append('0')
            frac /= 2
    return ''.join(result[::-1])

if __name__ == '__main__':
    assert(fractionToBin(0.625)) == '101'
    assert(fractionToBin2(0.625)) == '101'
