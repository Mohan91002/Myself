import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.exponential(scale = 2, size = (2,3))
print(x)
print()

# sns.distplot(random.exponential(scale = 2, size = (2,3)))
# plt.show()
# print()

sns.distplot(random.exponential(size = 1000), hist = False)
plt.show()