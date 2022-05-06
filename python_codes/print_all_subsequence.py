#!/usr/bin/python
import copy
def print_all_subsequence(string, target=[], output=[]):
    for i in range(len(string)):
        newtarget = copy.copy(target)
        newtarget.append(string[i])
        newstring=string[i+1:]
        output.append(newtarget)
        print_all_subsequence(newstring,newtarget,output)

def powerset(array):
	results = []
	powerSetUtil(array, [], results)
	return results

def powerSetUtil(array, result, results):
	if array:
		powerSetUtil(array[1:], result + [], results )
		powerSetUtil(array[1:], result + [array[0]], results )
	else:
		results.append(result)

if __name__ == '__main__':
    output=[]
    print_all_subsequence(string=raw_input(), target=[], output=output)
    print map(lambda x: ''.join(x), output)
