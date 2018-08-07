'''
author : teja
date : 7/8/2018
'''
def iterPower(base, exp):
    power = 1
    i=1
    whlie (i <= exp)
    power = power * base
    i++
    return power


def main():

    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()