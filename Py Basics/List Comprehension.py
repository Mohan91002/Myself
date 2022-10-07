import os
os.system("cls")

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = []
for x in my_list1:
       if "r" in x:
              my_list2.append(x)
print(my_list2)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = []
for x in my_list1:
       if "u" in x:
              my_list2.append(x)
print(my_list2)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = [ x for x in my_list1 if "u" in x]
print(my_list2)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = [ x for x in my_list1 if x != "mohan"]
print(my_list2)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = [ x for x in my_list1]
print(my_list2)
print()

newlist = [x for x in range(10)]
print(newlist)
print()

newlist = [x for x in range(10) if x <5]
print(newlist)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = [ x.upper() for x in my_list1]
print(my_list2)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list2 = [ "radha" for x in my_list1]
print(my_list2)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", "radha"]
my_list1.sort()
print(my_list1)
print()

my_list1 = [143, 110, 14, 4]
my_list1.sort()
print(my_list1)
print()

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print()

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
print()

def myfunc(n):
       return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print()