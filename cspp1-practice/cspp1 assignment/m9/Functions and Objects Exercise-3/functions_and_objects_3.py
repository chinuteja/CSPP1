#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]


def apply_to_each(List_1, int):
    for i in range(len(List_1)):
        List_1[i] = int(List_1[i])**2
    print(List_1)
    
    
def main():
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    apply_to_each(list1, int)

if __name__== "__main__":
    main()