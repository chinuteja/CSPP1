string = str(input("enter a string......  "))
a = 0
string2 = ""
for i in range(len(string)):
    a = ord((string[i:i+1]))
    print("value of ",a)
    if a%2 == 0:
        string2 = string2 + "0"
    else:
        string2 = string2 + "1"
print("result........",string2)
