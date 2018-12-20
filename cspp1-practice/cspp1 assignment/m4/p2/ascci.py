string_1 = str(input("enter a string......  "))
a_1 = 0
string_12 = ""
for i in range(len(string)):
    a_1 = ord((string_1[i:i+1]))
    print("value of ", a_1)
    if a_1%2 == 0:
        string_12 = string_12 + "0"
    else:
        string_12 = string_12 + "1"
print("result........", string_12)
