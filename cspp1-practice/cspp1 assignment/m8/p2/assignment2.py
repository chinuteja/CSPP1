'''
author : teja
date : 7/8/2018
'''

def sumofdigits(n_1):
    '''
    this function is used to calculate sum of digits of a given number
    '''
    if n_1 == 0:
        return 0
    return n_1%10+sumofdigits(n_1//10)
def main():
    '''
    main
    '''
    a_1 = input()
    print(sumofdigits(int(a_1)))
if __name__ == "__main__":
    main()
