#!/usr/bin/python
def squareRoot(number):
    return squareRootUtil(number, 1, number)

def squareRootUtil(number, low, high):
    if high < low:
        return -1
    guess = low + ( high - low ) / 2
    resultOfGuess = guess * guess 
    if resultOfGuess == number:
        return guess
    else:
        if resultOfGuess > number:
            return squareRootUtil(number, low, guess -1)
        else:
            return squareRootUtil(number, guess + 1 , high)

if __name__ == '__main__':
    print squareRoot(25)
    print squareRoot(35)
    print squareRoot(16)
    print squareRoot(100)
