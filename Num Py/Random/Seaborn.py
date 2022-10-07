import os
import numpy as np
from numpy import histogram, random
import matplotlib as mat
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()
# print()

sns.distplot([0, 1, 2, 3, 4, 5], hist = False)
plt.show()