  '''
author : teja
date : 4/8/2018
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    n_n = input()
    s_s = " "
    for i_i in n_n:
        if i_i in "!@#$%^&*/-" :
            i_i = ' '
            s_s = s_s + i_i
        else:
            i_i = i_i
            s_s = s_s + i_i
    print(s_s)
    
if __name__ == "__main__":
    main()