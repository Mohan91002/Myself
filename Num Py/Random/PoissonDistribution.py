import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.poisson(lam=2, size=10)
print(x)
print()

# sns.distplot(random.poisson(lam = 2, size = 1000), hist = True , kde = True)
# plt.show()
# print()

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()