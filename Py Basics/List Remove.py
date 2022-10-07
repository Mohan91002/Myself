import os
os.system("cls")

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list1.remove("07/05/1995")
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list1.pop(2)
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list1.pop()
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
del my_list1[2]
print(my_list1)
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
del my_list1
print()

my_list1 = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list1.clear()
print(my_list1)
print()