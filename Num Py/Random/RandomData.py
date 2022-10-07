import os
from numpy import random
os.system("cls")

x = random.choice([3, 5, 7, 9], p=[1, 0.0, 0.0, 0.0], size=(100))
print(x)
print()

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)