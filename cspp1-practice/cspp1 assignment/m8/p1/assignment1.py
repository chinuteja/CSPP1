'''
author : teja
date : 7/8/2018
'''
def factorial(n_1):
    '''
    this function is used to calclate factorial of a given number
    '''
    if n_1 in (0, 1):
        return 1
    return n_1*factorial(n_1-1)
def main():
    '''
    main
    '''
    a_1 = input()
    print(factorial(int(a_1)))

if __name__ == "__main__":
    main()
