import os
os.system("cls")

x = "Orange"
y = "Banana"
z = "Cherry"
print(x)
print(y)
print(z)
print()

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print()

x = y = z = "Orange"
print(x)
print(y)
print(z)
print()

fruits = ["apple", "banana", "cherry"] #unpack
x, y, z = fruits
print(x)
print(y)
print(z)
print()

fruits = ("apple", "banana", "cherry") #unpack
x, y, z = fruits
print(x)
print(y)
print(z)
print()