import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(np.diff(a))
print()

a = np.array([1, 12, 3, 14, 5, 16, 7])
print(np.diff(a, n = 2))
print()