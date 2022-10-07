import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

x = np.random.normal(170, 10, 25)
plt.hist(x)
plt.show()