'''
author : teja
date : 3/8/2018
'''

def main():
    '''
    this function is to check if the given number is perfect cube or not
    '''
    s_1 = int(input())
    answer = 0
    while answer**3 < s_1:
        answer = answer + 1
    if answer**3 == s_1:
        print(str(s_1) + " is perfect cube")
    else:
        print(str(s_1) + " is not a perfect cube")

if __name__ == "__main__":
    main()
