import os
import numpy as np
from numpy import random
from scipy import stats
import matplotlib.pyplot as plt
os.system("cls")

# x = np.array([60, 70, 80, 90, 100, 95, 85])
# y = np.array([65, 75, 85, 95, 105, 90, 80])
# plt.xlabel("ages")
# plt.ylabel("speed")
# plt.scatter(x, y)
# plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()
print()