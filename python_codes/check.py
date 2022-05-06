
def pre_process_pattern(input):
    prefix_matrix = [0 for _ in range(len(input))]
    j=0
    for i in range(1, len(input)):
        while j >0 and input[j] != input[i]:
            j=prefix_matrix[j-1]
        if input[j] == input[i]:
            j=j+1
        prefix_matrix[i] = j 
    return prefix_matrix

if __name__ == '__main__':
    ex_text = 'aaabb'
    print (pre_process_pattern(ex_text))
