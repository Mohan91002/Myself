import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a.shape)
print()

a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(a.shape)
print()

a = np.array([1, 2, 3, 4], ndmin = 5)
print(a.shape)
print()