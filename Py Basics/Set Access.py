import os
os.system("cls")

a = set(("munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"))
for x in a:
       print(x)
print()

a = {"munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"}
for x in a:
       print(x)
print()

a = {"munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"}
if "munna" in a:
       print(a)
else:
       print("No")
print()

a = {"munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"}
if "Munna" in a:
       print(a)
else:
       print("No")
print()

a = {"munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"}
if "munna" in a:
       print("munna" in a)
else:
       print("No")
print()

a = {"munna","kothi", "mohan", "faa", "kumar", "kumar", "kumar"}
if "Munna" in a:
       print("munna" not in a)
else:
       print("munna" in a)
print()