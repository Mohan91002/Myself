import os
import numpy as np
from cmath import log
os.system("cls")

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.add(a, b)
print(c)
print()

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.sum([a, b])
print(c)
print()

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.sum([a, b], axis = 1)
print(c)
print()

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.cumsum([a, b])
print(c)
print()

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.cumsum([a, b], axis = 1)
print(c)
print()

a = np.array([1, 2, 3])
c = np.cumsum([a])
print(c)
print()

a = np.array([1, 2, 3])
c = np.cumsum([a], axis = 1)
print(c)
print()