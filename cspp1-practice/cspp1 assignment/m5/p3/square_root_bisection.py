'''
author : teja
date : 5/8/2018
'''
def main():
    '''
    this function is used to find square root of a given number using bisection method
    '''
    square_root = int(input())
    epsilon = 0.01
    low_value = 0
    high_value = square_root
    answer = (low_value + high_value)/2
    while abs(answer**2-square_root) >= epsilon:
        if answer**2 < square_root:
            low_value = answer
        else:
            high_value = answer
        answer = (low_value + high_value)/2
    print(answer)
if __name__ == "__main__":
    main()
