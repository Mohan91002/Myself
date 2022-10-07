import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.binomial(n=10, p=0.5, size=10)
print(x)
print()

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=True)
# plt.show()
# print()

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
