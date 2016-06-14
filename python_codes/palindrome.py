#!/usr/local/bin/python
def isPal(x):
    def checkForPalindrome(x,y):
        if (x < 0):   
            return False  ## If negative then return false
        div = 1
        while (x / div >=10):
            div = div * 10
        while(x != 0):
            left = x / div
            right = x % 10
            if (left != right):
                return False
            x = (x % div) / 10 # Slash left and right part
            div = div / 100   # Since the no of digit are made two short (after slashing left and right digit)
        return True
    return checkForPalindrome(x,x)   # Hence reduce the scope of div

## Recursive way to do it
## The idea is to move to left digit of x and then comparing the left and right.
## After that move one to right side from left and move one to left from right
def isPalRecursive(x,y):
    if (x < 0):
        return False
    if (x == 0):
        return True
    if (isPalRecursive(x / 10 , y) and (x % 10 == y[0] % 10) ):  ## when the call goes to the called of recursive fun it actually has the value of x with first right digit included 
        y[0] /= 10  ## Move one step to left from right 
        return True
    else:
        return False


if __name__ == "__main__":
    number = raw_input("Enter the no \n")
    if (number.isdigit()):
        print (isPal(int(number)))
    else:
        print False
    print isPalRecursive(int(number) , [int(number)]) 
