import os
import numpy as np
os.system("cls")

a = np.array([4, 6, 3])
b = np.array([14, 16, 18])
print(np.gcd(a,b))
print()

a = np.array([4, 6, 8])
print(np.gcd.reduce(a))
print()

# a = np.array([4, 6, 8])
# print(np.gcd(a))
# print()

a = np.arange(1, 11)
x = np.gcd.reduce(a)
print(x)