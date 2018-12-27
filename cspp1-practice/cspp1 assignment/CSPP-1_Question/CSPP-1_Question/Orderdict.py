# from collections import OrderedDict
# d = OrderedDict()
# for _ in range(int(input())):
#     item,space,quantity = input().rpartition(' ')
#     # print("item...........",item)
#     # # print("space...........",space)
#     # print("quantity...........",quantity)
#     d[item] = d.get(item, 0) + int(quantity)
#     # print("item........",item)
#     # print("quantity..........",quantity)
# # print(".............",d.items())
# for item, quantity in d.items():
#     # print(".............")
#     print(item, quantity)
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()
# print("result..........",result)

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)
# print("result.........",result)

# Converting itertor to set
resultSet = set(result)
print(resultSet)