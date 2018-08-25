'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
     n = int(input())
     #print(n)
     s = ""
     for i in range  (n) :
        s += input()
     print(s)
     print()

if __name__ == '__main__':
    main()
