'''
author : teja
date : 6/8/2018
'''

def square(x):
    '''
    x: int or float.
    '''
    x=x**2
    return x   
# Correct

def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

