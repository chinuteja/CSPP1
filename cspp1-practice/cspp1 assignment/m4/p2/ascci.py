Strin_g1 = str(input("enter a string......  "))
A_a1 = 0
Strin_g2 = ""
for i in range(len(Strin_g1)):
    A_a1 = ord((Strin_g1[i:i+1]))
    print("value of ", A_a1)
    if A_a1%2 == 0:
        Strin_g2 = Strin_g2 + "0"
    else:
        Strin_g2 = Strin_g2 + "1"
print("result........", Strin_g2)
