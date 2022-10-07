import os
os.system("cls")

f = "radha {}" 
g = 25
print(f.format(g))
print()

age = 26
dob = "10/5/1995"
txt = "mohan kumar {}, {}"
print(txt.format(age,dob))
print()

age = 26
dob = "10/5/1995"
txt = "mohan kumar {1}, {0}"
print(txt.format(age,dob))
print()