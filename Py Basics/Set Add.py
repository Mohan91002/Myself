import os
os.system("cls")

a = {"munna", "mohan", "kumar", "satyavarapu"}
a.add("radha")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
a.update(b)
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu"}
b = ["munna", "mohan", "kumar", "satyavarapu", "radha"]
a.update(b)
print(a)
print()