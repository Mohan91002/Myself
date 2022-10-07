import os
from turtle import right
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7, 7, 7]) 
b = np.where( a == 7)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
b = np.where( a%2 == 0)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
b = np.where( a%2 == 1)
print(b)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.searchsorted(a, 7)
print(x)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.searchsorted(a, 7, side = 'right')
print(x)
print()

a = np.array([1, 3, 5, 7])
x = np.searchsorted(a, [2, 4, 6])
print(x)