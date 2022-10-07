import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a.dtype)
print()

a = np.array(['1', '2', '3', '4', '5', '6', '7'])
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='S')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='i')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='S4')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='i4')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='f4')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='U4')
print(a)
print(a.dtype)
print()

a = np.array([1, 2, 3, 4], dtype='u4')
print(a)
print(a.dtype)
print()

a = np.array(['a', 2, 3, 4])
print(a)
print(a.dtype)
print()

# a = np.array(['a', 2, 3, 4], dtype='i')
# print(a)
# print(a.dtype)
# print()

a = np.array([1.43, 2.25, 3.41, 4.31])
b = a.astype('i')
print(b)
print()

a = np.array([1.43, 2.25, 3.41, 4.31])
b = a.astype(int)
print(b)
print()

a = np.array([1, 2, 3, 4, 0])
b = a.astype(bool)
print(b)