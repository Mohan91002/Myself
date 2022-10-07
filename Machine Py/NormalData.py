import os
import numpy as np
from numpy import random
from scipy import stats
import matplotlib.pyplot as plt
os.system("cls")

x = np.random.normal(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()