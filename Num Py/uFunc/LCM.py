import os
import numpy as np
os.system("cls")

a = np.array([4, 6, 8])
b = np.array([14, 16, 18])
print(np.lcm(a,b))
print()

a = np.array([4, 6, 8])
print(np.lcm.reduce(a))
print()

# a = np.array([4, 6, 8])
# print(np.lcm(a))
# print()

a = np.arange(1, 11)
x = np.lcm.reduce(a)
print(x)