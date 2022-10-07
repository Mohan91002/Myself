import os
from numpy import histogram, random
from matplotlib import pyplot as plt, scale
import seaborn as sns
os.system("cls")

x = random.rayleigh(scale = 1, size = (2,3))
print(x)
print()

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()