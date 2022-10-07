import os
from numpy import random, size
os.system("cls")

x = random.randint(100)
print(x)
print()

x = random.rand()
print(x)
print()

x = random.randint(100, size = 7)
print(x)
print()

x = random.randint(100, size = (7)) # prefered
print(x)
print()

x = random.randint(100, size = (3,5)) # prefered
print(x)
print()

x = random.rand(5)
print(x)
print()

x = random.rand(3, 5)
print(x)
print()

x = random.choice([1, 2, 3,4, 5])
print(x)
print()

x = random.choice([1, 2, 3,4, 5], size = (3, 5))
print(x)