'''
author : teja
date : 4/8/2018
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    n_1 = len(str_input)
    i = 0
    for i in range(0, n_1):
        if str_input[i] == '@' or str_input[i] == '!' or str_input[i] == '#' or str_input[i] == '$' or str_input[i] == '%' or str_input[i] == '*' or str_input[i] == '^':
            str_input[i] = print(" "+str_input[i])
    print(str_input[i])
if __name__ == "__main__":
    main()