#!/usr/bin/python
def kWeakestRows(mat, k):

    # Note that there is a more conscise solution just below. This code 
    # avoids the use of advanced language features.

    m = len(mat)
    n = len(mat[0])
    
    # Calculate the strength of each row.
    strengths = []
    for i, row in enumerate(mat):
        strength = 0
        for j in range(n):
            if row[j] == 0: break
            strength += 1
        strengths.append((strength, i))
        
    # Sort all the strengths. This will sort firstly by strength
    # and secondly by index.
    strengths.sort()
    
    # Pull out and return the indexes of the smallest k entries.
    indexes = []
    for i in range(k):
        indexes.append(strengths[i][1])
    return indexes

if __name__ == '__main__':
    row = int(raw_input("enter number of rows "))
    col = int(raw_input("enter number of columns "))
    rows = []*row
    for i in range(0, row):
        rowvalues = map(lambda x : int(x), raw_input("enter values for rows {i}".format(i = i)).split(","))
        rows.append(rowvalues)
    print kWeakestRows(rows, 2)
