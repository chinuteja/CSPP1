'''
author : teja
date : 5/8/2018
'''

def main():
    '''
    function is to create squareroot of a number using approximation method
    '''
    square_root = int(input())
    epsilon = 0.01
    guess = 0.0
    step = 0.1
    while abs(guess**2 - square_root) > epsilon and guess <= square_root:
        guess = guess + step
    if abs(guess**2 - square_root) > epsilon:
        print(square_root)
    else:
        print(guess)
if __name__ == "__main__":
    main()
