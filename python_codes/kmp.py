def pre_process_pattern(input):
    prefix_matrix = [0 for _ in range(len(input))]
    k = 0
    for i in range(1, len(input)):
        while k > 0 and input[k] != input[i]:
            k = prefix_matrix[k-1]
        if input[k] == input[i]:
            k = k+1
        prefix_matrix[i] = k
    return prefix_matrix


def find_all_occurrence(t, p):
    prefix_matrix = pre_process_pattern(p)
    print (prefix_matrix)
    q = 0
    for i in range(len(t)):
        while q > 0 and p[q] != t[i]:
            q = prefix_matrix[q-1]
        if p[q] == t[i]:
            q = q+1
        if q == len(p):
            print ('Found match at %d' % (i - q + 1))
            q = prefix_matrix[q-1]


if __name__ == '__main__':
    text = 'bacbabababcaabcbab'
    pattern = 'abababca'
    #find_all_occurrence(text, pattern)
    print (pre_process_pattern(pattern))