
  
# function used for removing nested  
# lists in python. 
output = []  
def reemovNestings(l):
    global output
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
  
# Driver code 
def main():
    l = eval(input())
  
# output listoutput = [] 
    # print ('The original list: ', l) 
    reemovNestings(l) 
    print (sum(output)) 
if __name__ == '__main__':
    main()