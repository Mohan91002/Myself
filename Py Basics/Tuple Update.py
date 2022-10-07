import os
os.system("cls")

a = ("Mohan", "Kumar", "Satyavarapu", "Radha", "Mohan")
b = list(a)
b[1] = "Faa" 
a = tuple(b)  
print(a)
print()

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print()

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
print()

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y       #      thistuple = thistuple + y
print(thistuple)
print()

a = ("Mohan", "Kumar", "Satyavarapu", "Radha", "Mohan")
b = list(a)
b.remove("Satyavarapu")
a = b
print(a)
print()

a = ("Mohan", "Kumar", "Satyavarapu", "Radha", "Mohan")
b = list(a)
b.remove("Satyavarapu")
a = tuple(b)
print(a)
print()

thistuple = ("apple", "banana", "cherry")
del thistuple
print()