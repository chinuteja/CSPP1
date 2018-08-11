'''
   author :teja
   date : 11/8/2018
'''

def create_social_network(data):
    '''
     program used to convert the given data into dictonary.
    '''
    n_1 = data()
    l_1 = []
    for i_1 in range(len(str(n_1))):
        l_1.append(data())
        i_1 += i_1
    adict = {}
    for i_1 in l_1:
        l_2 = i_1.split(':')
        if l_2[0] in adict:
            l_2[1] = l_2[1].split(',')
            for j_1 in l_2[1]:
                adict[l_2[0]].append(int(j_1))
        else:
            l_2[1] = l_2[1].spilt(',')
            adict[l_2[0]] = l_2[1]
    print(adict)
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(str))

if __name__ == "__main__":
    main()
