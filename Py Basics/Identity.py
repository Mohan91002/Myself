import os
os.system("cls")

x = ["apple", "banana"]	
y = ["apple", "banana"]	
z = x
print(x is z)
print(x is y)
print(x == y)
print()

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)
print()