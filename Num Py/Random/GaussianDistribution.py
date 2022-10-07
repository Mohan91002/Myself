import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.normal(size=(2, 3))
print(x)
print()

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print()

sns.distplot(random.normal(size=1000), hist=False)
plt.show()