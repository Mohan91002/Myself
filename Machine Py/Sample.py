import os
import numpy as np
from scipy import stats
os.system("cls")

speed = np.array([60, 70, 80, 90, 100, 95, 85])
print(np.mean(speed))
print()

speed = np.array([60, 70, 80, 90, 100, 95, 85])
print(np.median(speed))
print()

speed = np.array([60, 70, 80, 90, 100, 95, 85, 85, 94, 7])
print(stats.mode(speed))