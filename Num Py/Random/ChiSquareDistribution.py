import os
from numpy import histogram, random
from matplotlib import pyplot as plt
import seaborn as sns
os.system("cls")

x = random.chisquare(df=2, size= (2,3))
print(x)
print()

sns.distplot(random.chisquare(df=2, size = 1000),hist = False)
plt.show()