import os
import numpy as np
os.system("cls")

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(np.unique(a))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 13, 14])
print(np.union1d(a,b))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 12, 13, 14])
print(np.intersect1d(a, b, assume_unique=True))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 12, 13, 14])
print(np.setdiff1d(a, b, assume_unique=True))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15])
print(np.setdiff1d(a, b))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15])
print(np.setxor1d(a, b))
print()

a = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
b = np.array([8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15])
print(np.setdiff1d(a, b, assume_unique=True))