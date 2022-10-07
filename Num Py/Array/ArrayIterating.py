import os
import numpy as np
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for x in a:
       print(x)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for x in a:
       print(a)
print()

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in a:
       print(x)
print()

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in a:
       print(a)
print()

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in a:
       for y in x:
              print(y)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
for x in a:
       print(x)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in a:
       for y in x:
              print(y)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in a:
      print(x)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in a:
       for y in x:
              for z in y:
                     print(z)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in np.nditer(a):
      print(x)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in np.nditer(a, flags=['buffered'], op_dtypes=['S']):
      print(x)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for x in np.nditer(a[:,::2]):
       print(x)
print()

a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],[13, 14, 15, 16]]])
for idx, x  in np.ndenumerate(a):
       print(idx, x)