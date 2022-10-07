import os
import numpy as np
from cmath import log
os.system("cls")

a = np.arange(1, 10)
print(np.log2(a))
print()

a = np.arange(1, 10)
print(np.log10(a))
print()

a = np.arange(1, 10)
print(np.log(a))
print()

a = np.frompyfunc(log, 2, 1)
print(a(100, 15))