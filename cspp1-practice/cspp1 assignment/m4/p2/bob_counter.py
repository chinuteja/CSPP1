'''
author:teja
date:8/2/2018
'''

def main():
    '''
    this function gives no of bobs in a string
    '''

    s_1 = input()
    x_1 = len(s_1)
    y_1 = "bob"
    count = 0
    for i in range(0, x_1, 1):
        if s_1[i:i+3] == y_1:
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()
