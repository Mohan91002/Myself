import os
import numpy as np
from numpy.lib.function_base import copy
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = copy(a)
print(a)
print()
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.copy()
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.copy()
a[0] = 8
print(a)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a)
b = a.copy()
b[0] = 8
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.view()
a[0] = 8
print(a)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.view()
b[0] = 8
print(a)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.view()
b[0:7] = [8, 9, 10, 11, 12, 13, 14]
print(a)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.view()
b[0:7] = [8, 9, 10, 11, 12, 13, 14]
print(a)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a.copy()
c = a.view()
print(b)
print()
print(c)
print()
print(b.base)
print()
print(c.base)