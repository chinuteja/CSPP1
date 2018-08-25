'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    count = dict()
    words = string.split()
    for i in words:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
        return count

            
def main():
    #n = int(input())
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
