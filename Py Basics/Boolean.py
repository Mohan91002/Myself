import os
os.system("cls")

print(10 == 9)
print()

print(10 == 10)
print()

print(10 > 9)
print()

print(10 < 9)
print()

a = 10
b = 7
if b > a:
       print("b is greater than a")
else:
       print("b is not greater than a")
print()

print(bool("munna"))
print()

print(bool(5))
print()

print(bool(12.25))
print()

a = 20
print(bool(a))
print()

b = "munna"
print(bool(b))
print()

c = 12.25
print(bool(c))
print()

print(bool("12.25",))
print()

print(bool("12.25"))
print()

print(bool(["munna","mohan"]))
print()

print(bool())
print()

print(bool([]))
print()

class myclass():
       def __len__(self):
              return 0
myobj = myclass()
print(bool(myobj))
print()

def myFunc():
       return True
print(myFunc())

def myFunction():
       return True
if myFunction():
       print("YES!")
else:
       print("NO!")
print()

def myFunction():
       return False
if myFunction():
       print("YES!")
else:
       print("NO!")
print()

x = 200
print(isinstance(x, str))
print()