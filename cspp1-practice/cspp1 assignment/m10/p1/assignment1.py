'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    
    str_1 = 'abcdefghijklmnopqrstuvwxyz'
    letters_guessed = ['a','b','c','a','d','d']
    str_a = list(str_1)
    x = len(letters_guessed)
    for i in  range (x) :
        if letters_guessed[i] in  str_a:
            str_2 = str_a.remove(letters_guessed[i])
    return ''.join(str_a)



def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
