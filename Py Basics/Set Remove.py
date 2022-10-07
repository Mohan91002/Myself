import os
os.system("cls")

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.remove("radha")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.remove("mohan")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.discard("munna")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.discard("faa")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.pop()
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
a.clear()
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "mohan"}
del a                              # print show error
print()