'''
author : teja 
date : 9/8/2018
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    string_s = 'abcdefghijklmnopqrstuvwxyz'
    print('welcome to hangman game')
    print('I am thinking of a w', len(secretWord),"letters long")
    print('-----------')
    str_list =list(string_s)
    secret_list = list(secretWord)
    samp = list(secretWord)
    temp = ""
    won = 1
    l1 =[]
    for i in secretWord:
        temp = temp +"_"
    samp=list(temp)
    guesses = 8
    while (guesses>0):
        if ''.join(samp) == secretWord:
            won = 1
            print("you won")
            break

        print('you have', guesses,'guesses left')
        print("Availbe letters",''.join(str_list))
        let = input()
        if let in l1:
            print("you have entered this letter")
        else:
            l1.append(let)
            if let in secret_list:
                for j in range(len(secretWord)):
                    if let == secret_list[j]:
                        samp[j]=let
                str_list.remove(let)
                print("Good guess :", ''.join(samp))
            else:
                guesses-=1
                str_list.remove(let)
                print("oops letter is not my word" ''.join(samp))
                print("---------")
        if won == 0:
            print('you lost',secretWord)


        pass

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
