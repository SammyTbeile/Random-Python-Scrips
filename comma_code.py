'''
Function that takes a list and converts it to a string
Author: Sammy Tbeile
June 11 2017
'''

def comma_code(list):
	ret_val = ''
	for i in range(len(list)):
		if i == (len(list)) -1:
			ret_val += "and " + list[i]
		else:
			ret_val += list[i] + ", "
	return ret_val


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
