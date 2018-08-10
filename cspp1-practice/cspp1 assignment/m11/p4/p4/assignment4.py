''' 
author : teja
date : 10/8/2018
'''
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    """
   sum_v = 0
   for i_1 in hand:
       sum_v = sum_v + hand[i_1]
    return sum_v
def main():
	'''
	main
	'''
	n = input()
	adict = {}
	for i_1 in range(int(n_1)):
		data=input()
		l_1=data.split()
		adict[l_1[0]]=int(l_1[1])
	print(calculateHandlen(adict))
if __name__== "__main__":
	main()