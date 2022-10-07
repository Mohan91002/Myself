import os
import numpy as np
os.system("cls")

x = np.sin(np.pi/2)
print(x)
print()

x = np.cos(np.pi/2)
print(x)
print()

x = np.tan(np.pi/2)
print(x)
print()

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6, np.pi/9])
a = np.sin(x)
print(a)
print()

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6, np.pi/9])
a = np.cos(x)
print(a)
print()

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6, np.pi/9])
a = np.tan(x)
print(a)
print()

x = np.array([90, 60, 45, 36, 30, 20])
a = np.deg2rad(x)
print(a)
print()

x = np.array([90, 60, 45, 36, 30, 20])
a = np.rad2deg(x)
print(a)
print()

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5, np.pi/6, np.pi/9])
a = np.arcsin(x)
print(a)
print()

x = np.arcsin(1.0)
print(x)
print()

x = np.array([1, 0, -1])
a = np.arcsin(x)
print(a)
print()

base = 3
perp = 4
x = np.hypot(base, perp)
print(x)