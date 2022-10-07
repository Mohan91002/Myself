import os
os.system("cls")

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.union(b)
print(c)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
a.update(b)
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
a.intersection_update(b)
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.intersection(b)
print(c)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
a.symmetric_difference_update(b)
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.symmetric_difference(b)
print(c)
print()

