'''
author = teja
date = 8/4/2018
'''

def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    if num > 0:
        for i in range(1, num+1, 1):
            if i%3 == 0 and i%5 == 0:
                print("FizzBuzz")
            elif i%5 == 0:
                print("Buzz")
            elif i%3 == 0:
                print("Fizz")
            else:
                print(i) 
if __name__ == "__main__":
    main()