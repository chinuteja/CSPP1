#Exercise : Odd Tuples
#author : teja
#date:8/8/2018

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    return aTup[::2]

def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (str(data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()