import os
import numpy as np
from numpy import random
from scipy import stats
import matplotlib.pyplot as plt
os.system("cls")

# x = np.random.uniform(0.0, 5.0, 250)
# print(x)
# print()

# x = np.random.uniform(0.0, 5.0, 250)
# plt.plot(x)
# plt.show()
# print()

# x = np.random.uniform(0.0, 5.0, 250)
# plt.hist(x, 5)
# plt.show()
# print()

# x = np.random.uniform(0.0, 5.0, 250)
# plt.hist(x)
# plt.show()

x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()