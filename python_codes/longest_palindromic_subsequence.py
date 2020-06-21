import sys

def printSubStr(st,low,high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

def longestPalSubstr(st) :
    n = len(st) # get length of input string

    table = [[0 for x in range(n)] for y
             in range(n)]

    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1

    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    k = 3
    while k <= n :
        i = 0
        while i < (n - k + 1) :
            j = i + k - 1

            if (table[i + 1][j - 1] and
                    st[i] == st[j]) :
                table[i][j] = True

                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1
    printSubStr(st, start,
            start + maxLength - 1)
    return maxLength

def max(x, y):
    if(x > y):
        return x
    return y

def lps(seq, i, j):

    if (i == j):
        return 1

    if (seq[i] == seq[j] and i + 1 == j):
        return 2

    if (seq[i] == seq[j]):
        return lps(seq, i + 1, j - 1) + 2

    return max(lps(seq, i, j - 1),
               lps(seq, i + 1, j))


def getScore(s):
    maxScore = 0
    for i in range(0, len(s)):
        temp = lps(s, 0, i) * lps(s, i, len(s) -1)
        if maxScore < temp:
            maxScore = temp
    return maxScore


#st = "forgeeksskeegfor"
st = "attract"
l = getScore(st)
print ("Length is:", l)

# This code is contributed by Nikita Tiwari.
