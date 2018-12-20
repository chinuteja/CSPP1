String_1 = str(input("enter a string......  "))
a_1 = 0
String_2 = ""
for i in range(len(String_1)):
    a_1 = ord((String_1[i:i+1]))
    print("value of ", a_1)
    if a_1%2 == 0:
        String_2 = String_2 + "0"
    else:
        String_2 = String_2 + "1"
print("result........", String_2)
