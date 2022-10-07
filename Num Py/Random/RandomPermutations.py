import os
import numpy as np
from numpy import random
os.system("cls")

a = np.array([1, 2, 3, 4, 5, 6, 7])
random.shuffle(a)
print(a)
print()

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = random.permutation(a)
print(b)