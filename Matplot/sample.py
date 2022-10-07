import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
os.system("cls")

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()