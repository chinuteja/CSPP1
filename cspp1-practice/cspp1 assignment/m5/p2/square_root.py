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
    num_guesses = 0
    while abs(guess**2 - square_root) > epsilon and guess <= square_root:
        guess = guess + step
        num_guesses = num_guesses + 1
    print("the number of gusses is", num_guesses)
    if abs(guess**2 - square_root) > epsilon:
        print("couldn't find the square root of given number", square_root)
    else:
        print("the square root of given number is ", guess)
if __name__ == "__main__":
    main()
