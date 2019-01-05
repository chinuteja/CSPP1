
  
# function used for removing nested  
# lists in python. 
output = []
count = 0  
def deepList(l):
    global output
    global count
    for i in l: 
        if type(i) == list: 
            count = count + 1
            deepList(i) 
        else: 
            output.append(i) 
  
# Driver code 
def main():
    l = eval(input())
  
# output listoutput = [] 
    # print ('The original list: ', l) 
    deepList(l)
    # print(output) 
    # print (sum(output))
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # beta = "dfgdfg"
    # gamma = "jkkk
    sum1 = 0 
    for i in output:
        if type(i) == str:
            continue
        else:
            sum1 = sum1 + i
    print(sum1)
    print(count)
if __name__ == '__main__':
    main()