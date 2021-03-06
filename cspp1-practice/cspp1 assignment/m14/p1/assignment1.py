'''
author : teja
date : 21/08/2018
'''
import string
class Cipher:
    '''
    method used for cipher
    '''
    def __init__(self, value):
        self.value = value

    def __len__(self):
        count = 0
        for i in self.value:
            count += 1
        return count

    def shift(self, shift_number):
        '''
        this function is used to return shifted string
        '''
        small_alphabet = ""
        upper_alphabet = ""
        small_alphabet = "-" + string.ascii_lowercase + string.ascii_lowercase
        upper_alphabet = "-" + string.ascii_uppercase + string.ascii_uppercase
        shifted_string = ""
        a_1 = len(self.value)
        for i in range(0, a_1):
            if self.value[i] in small_alphabet:
                shifted_string += small_alphabet[small_alphabet.index(self.value[i]) + shift_number]
            elif self.value[i] in upper_alphabet:
                shifted_string += upper_alphabet[upper_alphabet.index(self.value[i]) + shift_number]
            else:
                shifted_string += self.value[i]

        return shifted_string


def main():
    '''
        Function to handle testcases
    '''
    data_input = input()
    shift_number = int(input())
    Cipher_Obj = Cipher(data_input)
    print(Cipher_Obj.shift(shift_number))
    # print(Cipher.shift(data_input, shift_number))

if __name__ == "__main__":
    main()
