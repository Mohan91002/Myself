import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.uniform(size=(2, 3))
print(x)
print()

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()