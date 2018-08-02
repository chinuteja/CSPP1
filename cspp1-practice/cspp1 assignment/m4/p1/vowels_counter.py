'''
author:teja
date:8/2/2018
'''

def main():
    '''
    this function gives no of vowels
    '''

    s_1 = input()
    x_1 = len(s_1)
    count = 0
    for i in range(0, x_1, 1):
        if (s_1[i] == 'a' or  s_1[i] == 'e' or s_1[i] == 'i' or s_1[i] == 'u'or s_1[i] == 'o'):
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()
