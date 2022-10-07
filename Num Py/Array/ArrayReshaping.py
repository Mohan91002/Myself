import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a.reshape(4, 2)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a.reshape(2, 2, 2)
print(b)
print()

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b = a.reshape(3, 3)
# print(b)
# print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a.reshape(2, 4).base)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a.copy()
print(b.reshape(4,2).base)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a.reshape(2, 2, -1)
print(b)
print()

a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(a.reshape(-1))
print()

