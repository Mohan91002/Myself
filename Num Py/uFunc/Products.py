import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(np.product(a))
print()

a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8])
print(np.product([a,b]))
print()

a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8])
print(np.product([a,b], axis = 1))
print()

a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8])
print(np.cumprod([a,b], axis = 1))