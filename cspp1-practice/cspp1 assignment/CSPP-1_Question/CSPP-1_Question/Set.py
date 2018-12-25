list1 = [[1,2,3],[4,5,6]]
a = set()
# j = 0
for i in range(len(list1)):
    for j in range(len(list1[0])):
        a.add(list1[i][j])
        j = j + 1
        print(a)
