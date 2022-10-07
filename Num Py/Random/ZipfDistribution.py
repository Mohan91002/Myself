import os
from numpy import histogram, random
from matplotlib import pyplot as plt, scale
import seaborn as sns
os.system("cls")

x = random.zipf(a = 2, size = (2,3))
print(x)
print()

# sns.distplot(random.zipf(a = 2, size = 1000), hist = False)
# plt.show()
# print()

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()