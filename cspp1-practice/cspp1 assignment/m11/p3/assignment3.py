# Assignment-3
'''
author : teja
date : 10/8/2018
module 11
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    """
    count = 0
    word = list(word)
    for i in word:
        if i in hand:
            count += count 
        if count == len(word) and word[i] == wordList[i]:
            return True
    return False
        

def main():
    '''
    main
    '''
    word=input()
    n=int(input())
    adict={}
    for i in range(n):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    l2=input().split()
    print(isValidWord(word,adict,l2))
if __name__== "__main__":
    main()