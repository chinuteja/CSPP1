'''
author : teja
date : 25/8/2018
'''

def clean_string(string):
    string_1 = ""
    for i_1 in string:
        if i_1 in ".!@#$%^&*() ":
           i_1 = ""
           string_1 = string_1 + i_1
        else:
            i_1 = i_1
            string_1 = string_1 + i
    return string_1
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
