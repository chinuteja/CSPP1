# Assignment-3
'''
author : teja
date : 10/8/2018
module 11
'''

def is_valid_word(word_test, hand_word, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    """
    count = 0
    word_test = list(word_test)
    for i_1 in word_test:
        if i_1 in hand_word:
            count += count
        if count == len(word_test) and word_test[i_1] == word_list[i_1]:
            return True
        return False
def main():
    '''
    main
    '''
    word_test = input()
    n_1 = int(input())
    adict = {}
    for i_1 in range(n_1):
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_valid_word(word_test, adict, l_2))
if __name__ == "__main__":
    main()
