import os
import numpy as np
os.system("cls")

def add(x, y):
       return x+y
add = np.frompyfunc(add, 2, 1)
print(add([1, 2, 3, 4], [5, 6, 7, 8]))
print()

print(type(np.add))
print()

print(type(np.concatenate))
print()

''' print(type(np.blahblah))
print() '''

if type(np.add) == np.ufunc:
       print('add is ufunc')
else:
       print('add is not ufunc')
print()

