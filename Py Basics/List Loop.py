import os
os.system("cls")

my_list = ["Munna", "Mohan", "Leo", "Faa"]
for x in my_list:
       print(x)
print()

my_list = ["Munna", "Mohan", "Leo", "Faa"]
for x in range(len(my_list)):
                            print(x)
print()

my_list = ["Munna", "Mohan", "Leo", "Faa"]
for x in range(len(my_list)):
                            print(my_list[x])
print()

my_list = ["Munna", "Mohan", "Leo", "Faa"]
x = 0
while x < len(my_list):
                     print(my_list[x])
                     x = x + 1
print()

my_list = ["Munna", "Mohan", "Leo", "Faa"]
[print(x) for x in my_list]      
print()
