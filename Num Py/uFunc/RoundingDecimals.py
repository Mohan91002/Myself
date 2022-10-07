import os
import numpy as np
os.system("cls")

a = np.array([1.0, 2.54, 1.43, 2.25])
print(np.trunc(a))
print()

a = np.array([1.0, 2.54, 1.43, 2.25])
print(np.fix(a))
print()

a = np.array([1.1201, 2.54143, 1.43142, 2.25225])
print(np.around(a, 2))
print()

a = np.array([1.1201, 2.54143, 1.43142, 2.25225])
print(np.floor(a))
print()

a = np.array([1.1201, 2.54143, 1.43142, 2.25225])
print(np.ceil(a))
print()

