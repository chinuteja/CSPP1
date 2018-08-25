'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    l_1 = list(dictionary.values())
    l_2 = list(dictionary.keys())
    dict_testkeys = l_2[:]
    dict_testkeys.sort()
    for i in  dict_testkeys:
        dict_testkeys[i] = "#"
     return dict_testkeys

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
