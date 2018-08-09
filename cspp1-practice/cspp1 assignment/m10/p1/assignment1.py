'''
author : teja
date : 9/8/2018
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = 'abcdefghijklmnopqrstuvwxyz'
    str_a = list(str_1)
    x_1 = len(letters_guessed)
    for i in  range(x_1):
        if letters_guessed[i] in  str_a:
            str_a.remove(letters_guessed[i])
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
