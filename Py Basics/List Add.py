import os
os.system("cls")

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list.append("radha")
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list.insert(2,"radha")
print(my_list)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list2 = ["radha", "satya"]
my_list1.extend(my_list2)
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list2 = ("radha", "satya")
my_list1.extend(my_list2)
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list2 = {"radha", "satya"}
my_list1.extend(my_list2)
print(my_list1)
print()