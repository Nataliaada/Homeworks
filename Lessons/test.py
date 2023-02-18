from calendar import c

v = (1,2,3)
print(v)
print(type(v))


vc ={1, 2, 3}
print(vc)
print(type(vc))

vc ={1:"a", 2:"e", 3:"d"}
print(vc)
print(type(vc))

list = [i for i in range(1,10)]
print(list)

list = [(i,i) for i in range(1,10)]

print(list)
print(type(list))


list = [i**2 for i in range(9) if i%2==0]

print(list)