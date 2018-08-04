'''
author : teja
date : 8/4/2018
'''

def main():
    '''
    this function is to multiply the digits in a nubmber.
    '''
    int_input = int(input())
    x_1 = 1
    if int_input == 0:
        print("0")
    else:
        while int_input != 0:
            temp = int_input%10
            x_1 = x_1*temp
            int_input = int_input//10
        print(x_1)
if __name__ == "__main__":
    main()