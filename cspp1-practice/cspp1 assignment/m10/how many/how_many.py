'''
Author : Teja
Date : 9/8/2018
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count_value = 0
    for i in aDict:
    	count_value = count_value + len(aDict[i])
    return count_value
    
def main():
	n=input()
	aDict={}
	for i in range(int(n)):
		s=input()
		l=s.split()
		if l[0][0] not in aDict:
			aDict[l[0][0]]=[l[1]]
		else:
			aDict[l[0][0]].append(l[1])
	print(how_many(aDict))



if __name__== "__main__":
    main()