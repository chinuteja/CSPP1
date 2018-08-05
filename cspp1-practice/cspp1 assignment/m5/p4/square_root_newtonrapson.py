'''
author : teja
date : 5/8/2018
'''
def main():
    '''
    This function is to calculate square root of a given number by using newton raphson method
    '''
    square_root = int(input())
    epsilon = 0.01
    guess = square_root/2.0
    while (guess**2 - square_root) >= epsilon:
        guess = guess- ((guess**2 - square_root)/(2*guess))
    print(guess)
if __name__ == "__main__":
    main()
