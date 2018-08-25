'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    count = dict()
    words = string.split()
    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
    return count

            
def main():
    #n = int(input())
    string = input()
    print(string)
    print(tokenize(string))
    #print(tokenize(string=input()))

if __name__ == '__main__':
    main()
