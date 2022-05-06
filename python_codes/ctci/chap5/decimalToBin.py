#!/usr/bin/python

def decimalToBin(dec, rep = ''):
    if dec >= 1:
        return decimalToBin(dec//2, str(dec % 2) + rep)
    return rep if rep else '0'


print (decimalToBin(4))
print (decimalToBin(3))
print (decimalToBin(0))
