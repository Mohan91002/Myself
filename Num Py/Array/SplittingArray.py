import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array_split(a, 3)
print(b)
print()

a = np.array([1, 2, 3, 4, 5])
b = np.array_split(a, 3)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array_split(a, 4)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array_split(a, 4)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print()

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
b = np.array_split(a, 3)
print(b)
print()

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b = np.array_split(a, 3)
print(b)
print()

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b = np.array_split(a, 3, axis = 1)
print(b)
print()

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b = np.hsplit(a, 3)
print(b)
print()

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b = np.vsplit(a, 3)
print(b)
print()

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
b = np.dsplit(a, 3)
print(b)