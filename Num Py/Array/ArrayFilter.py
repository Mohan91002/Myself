import os
import numpy as np
os.system("cls")

a = np.array([41, 42, 43, 44])
b = [True, False, True, False]
c = a[b]
print(c)
print()

a = np.array([41, 42, 43, 44])
c = []                             # c == new filter array
for element in a:
       if element > 42:
              c.append(True)
       else:
              c.append(False)
b = a[c]
print(c)
print(b)
print()

a = np.array([41, 42, 43, 44])
c = []                             # c == new filter array
for element in a:
       if element%2 == 0:
              c.append(True)
       else:
              c.append(False)
b = a[c]
print(c)
print(b)
print()

a = np.array([41, 42, 43, 44])
b = a > 42
c = a[b]
print(b)
print(c)
print()

a = np.array([41, 42, 43, 44])
b = a%2 == 0
c = a[b]
print(b)
print(c)