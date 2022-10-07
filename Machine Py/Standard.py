import os
import numpy as np
from scipy import stats
os.system("cls")

speed = np.array([60, 70, 80, 90, 100, 95, 85])
print(np.std(speed))
print()

speed = np.array([60, 70, 80, 90, 100, 95, 85])
print(np.var(speed))
print()