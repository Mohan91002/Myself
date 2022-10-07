import os
os.system("cls")

my_list = ["mohan", "kumar", "satyavarapu"]
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'mohan']
print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'mohan']
print(len(my_list))
print()

my_list = ["mohan", "kumar", "satyavarapu", 'mohan', "07/05/1995"]
print(my_list)
print(type(my_list))
print()

my_list = [1, 2, 3, 4]
print(my_list)
print(type(my_list))
print()

my_list = [True, False, True]
print(my_list)
print(type(my_list))
print()

my_list = ["mohan", 26, True]
print(my_list)
print(type(my_list))
print()

my_list = list(("mohan", 26, True))
print(my_list)
print(type(my_list))
print()

my_list = list(("mohan", 26, True))
print(my_list[0])
print()

my_list = ["mohan", 26, True]
print(my_list[-1])
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
print(my_list[0:4])
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
print(my_list[-5:-1])
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
print(my_list[0:])
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
if "munna" in my_list:
    print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
if "radha" not in my_list:
    print(my_list)
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
if "munna" in my_list:
    print(my_list)
else:
    print("munna not in list")
print()

my_list = ["mohan", "kumar", "satyavarapu", 'munna', "07/05/1995"]
if "radha" in my_list:
    print(my_list)
else:
    print("radha not in list")
print()