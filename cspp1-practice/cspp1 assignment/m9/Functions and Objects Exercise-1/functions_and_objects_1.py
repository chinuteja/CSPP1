#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(List_1, abs):
    for i in range (len(List_1)):
    	List_1[i] = abs(List_1[i])
    print(List_1) 
def main():
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
