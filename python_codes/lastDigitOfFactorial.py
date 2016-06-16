def lastDigitOfFactorial(number):
    lastDigit = 1
    numberOfTwo = 1
    for i in range(3,number + 1):
        while ( i % 10 == 0):
            i /= 10
        while ( i % 2 == 0):
            numberOfTwo = numberOfTwo + 1
            i /= 2
        while ( i % 5 == 0):
            i /= 5
            numberOfTwo = numberOfTwo - 1
        lastDigit = ( i  * lastDigit ) % 10
    for i in range (0, numberOfTwo):
        lastDigit = ( lastDigit * 2 ) % 10
    return lastDigit

if __name__ == "__main__":
    number = input()
    print (lastDigitOfFactorial(int(number)))
