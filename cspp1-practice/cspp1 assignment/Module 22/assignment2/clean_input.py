'''
author : teja
date : 25/8/2018
'''

def clean_string(string):
	'''
	function to perform string operation
	'''
    string_1 = ""
    for i_1 in string:
        if i_1 in ".!@#$%^&*() ":
            i_1 = ""
            string_1 = string_1 + i_1
        else:
            i_1 = i_1
            string_1 = string_1 + i_1
    return string_1
def main():
	'''
	function to take input
	'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
