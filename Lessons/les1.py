
#
# n = int(input("Введите кол-во парт для класса А: "))
# m = int(input("Введите кол-во парт для класса Б: "))
# c = int(input("Введите кол-во парт для класса C: "))
# print((n+1)//2 + (m+1)//2 + (c+1)//2)
#
# 2
# list_1 = []
# for i in range(1,100):
#     list_1.append(i)

list_1 = [i for i in range(1, 6)]
print(list_1)

n = input('Введите число')  #012345
if n in range(0,2):
    return 1
else:
    return n*(n - 1)