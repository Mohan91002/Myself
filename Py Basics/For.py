import os
os.system("cls")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
       print(x)
print()

a = "Mohan"
for x in a:
       print(x)
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
       if x == "banana":
              break
       print(x)
print()


fruits = ["apple", "banana", "cherry"]
for x in fruits:
       print(x) 
       if x == "banana":
              break
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
       if x == "banana":
              continue
       print(x)
print()

for x in range(6):
       print(x)
print()

for x in range(7,17):
       print(x)
print()

for x in range(7,17,9):
       print(x)
print()

for x in range(6):
       print(x)
else:
       print("out of my range")
print()

for x in range(7,17):
       print(x)
else:
       print("out of my range")
print()

for x in range(7,100,9):
       print(x)
else:
       print("out of my range")
print()

for x in range(7):
       if x == 3: 
              break
              print(x)
       else:
              print("Finally finished!")
print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
       for y in fruits:
              print(x, y)
print()

for x in [0, 1, 2]:
       # print(x)
       pass
print()
