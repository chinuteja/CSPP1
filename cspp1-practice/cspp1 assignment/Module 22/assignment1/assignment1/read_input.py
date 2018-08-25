'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    number_lines = int(input())
    #print(n)
    string_1 = ""
    for i in range(number_lines):
        string_1 = input()
        print(string_1,end="")
        print()
if __name__ == '__main__':
    main()
