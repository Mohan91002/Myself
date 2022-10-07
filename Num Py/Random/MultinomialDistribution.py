import os
from numpy import histogram, random, size
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.multinomial(n = 6, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
print()

x = random.multinomial(n = 6, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size = (2,3))
print(x)
print()

sns.displot(random.multinomial(n = 6, pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]))
plt.show()