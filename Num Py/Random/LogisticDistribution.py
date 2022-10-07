import os
from numpy import histogram, random, size
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.logistic(loc=1, scale= 2, size=(2,3))
print(x)
print()

# sns.distplot(random.logistic(size=1000), hist=False)
# plt.show()
# print()

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()