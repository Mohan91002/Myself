import os
os.system("cls")

class my:
       x = 5
       print(x)
print()

class my:
       x = 5
print(my)
print()

class my:
       x = 5
y = my()
print(y.x)
print()

class Person:
       def __init__(self, name, age):
              self.name = name
              self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print()

class Person:
       def __init__(self, name, age):
              self.name = input("Enter Name: ")
              self.age = input("Enter Age: ")
       def myfunc(self):
              print("Hello my name is " + self.name + " " + self.age)
p1 = Person("", "")
p1.myfunc()
print()

class Person:
       def __init__(mysillyobject, name, age):
              mysillyobject.name = name
              mysillyobject.age = age
       def myfunc(abc):
              print("Hello my name is " + abc.name)
              print(abc.age)
p1 = Person("John", 36)
p1.myfunc()
print()

class Person:
       def __init__(self, name, age):
              self.name = name
              self.age = age
       def myfunc(self):
              print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)
print()

class Person:
       def __init__(self, name, age):
              self.name = name
              self.age = age
       def myfunc(self):
              print("Hello my name is " + self.name)
p1 = Person("John", 36)
print(p1.age)                                           # del p1
print()

class Person:
       pass