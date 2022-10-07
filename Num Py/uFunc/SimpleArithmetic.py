import os
import numpy as np
os.system("cls")

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.add(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.subtract(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.multiply(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.divide(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.power(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.mod(a, b)
print(c)
print()

a = np.array([10, 11, 12, 13, 14, 15])
b = np.array([20, 21, 22, 23, 24, 25])
c = np.remainder(b, a)
print(c)
print()

a = np.array([10, -11, 12, -13, 14, -15])
b = np.absolute(a)
print(b)