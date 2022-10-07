import os
os.system("cls")

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[0] = "munna"
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[0:] = ["radha", "radha", "radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[0:3] = ["radha", "radha", "radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[0:3] = ["radha", "radha", "radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[1] = ["radha", "radha", "radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[1:3] = ["radha", "radha", "radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list[1:6] = ["radha"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list.insert(4,"radha")
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list.insert(len(my_list),"radha")
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
my_list.insert(-4,"radha")
print(my_list)
print()