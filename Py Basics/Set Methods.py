import os
os.system("cls")

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
a.add("puspha")
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
a.clear()
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha"}
b = a.copy()
print(b)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.difference(b)
print(c)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
a.difference_update(b)
print(a)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
a.discard("vedu")
b.discard("vedu")
print(a)
print(b)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu", "puspha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.isdisjoint(b)
print(c)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu", "puspha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.issubset(b)
print(c)
print()

a = {"munna", "mohan", "kumar", "satyavarapu", "radha", "vedu", "puspha"}
b = {"munna", "mohan", "kumar", "satyavarapu", "radha", "puspha"}
c = a.issuperset(b)
print(c)
print()