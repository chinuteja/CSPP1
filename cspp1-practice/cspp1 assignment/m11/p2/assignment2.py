'''
author : teja
date : 10/8/2018
'''


def update_hand(hand_word, test_word):
    """
   this function is used to decrement the value of key by 1
   """
    test_word = list(test_word)
    for i_1 in test_word:
        if i_1 in hand_word:
            hand_word[i_1] = hand_word[i_1] - 1
    return hand_word
def main():
    '''
    main function
    '''
    n_1 = input()
    adict = {}
    for i_1 in range(int(n_1)):
        data = input()
        l_1 = data.split()
        i_1 += 1
        adict[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
