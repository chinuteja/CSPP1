'''
author: teja
date : 2/8/2018
'''

def main():
	'''
	This function gives alphabetical order of a string
	'''

	s_1 = input()
	c_1 = 0
	c_max = 0
	end_index = 0
	n_1 = len(s_1)
	for i in range((n_1)-1):
		if(ord(s_1[i]) <= ord(s_1[i+1])):
			c_1 = c_1 + 1
		else:
			c_1 = 0
		if (c_max < c_1):
			c_max = c_1
			end_index = i+1
	print(s_1[end_index-c_max : end_index+1])

if __name__ == "__main__":
	main()
