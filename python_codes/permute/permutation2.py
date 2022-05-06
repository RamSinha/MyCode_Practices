#!/usr/bin/python

def permute(string):
    permuteHelper("", string)

def permuteHelper(prefix, string):
    if len(string) == 0:
        print (prefix)
        return

    for idx in range(len(string)):
        # fill the slot with available option
        temp = string[:idx] + string[idx+1:]
        permuteHelper(prefix + string[idx], temp)

if __name__ == '__main__':
    permute('abc')
