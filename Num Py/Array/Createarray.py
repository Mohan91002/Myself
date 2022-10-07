import os
import numpy as np
os.system("cls")

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print()

arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(type(arr))
print()

arr = np.array({1, 2, 3, 4, 5})
print(arr)
print(type(arr))
print()

arr = np.array(42)                        # 0-D
print(arr)
print()

arr = np.array({1, 2, 3, 4, 5})           # 1-D
print(arr)
print()

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    # 2-D
print(arr)
print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])      #3-D
print(arr)
print()

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print()

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
print()

# a = print(np.array([1, 2, 3, 4], ndmin=5))
# print('number of dimensions :', a.ndim)