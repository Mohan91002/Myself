import os
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
os.system("cls")

a = np.arange(10)
b = 2*a + 1
d = interp1d(a, b)
c = d(np.arange(2.1, 3, 0.1))
print(c)
print()

a = np.arange(10)
b = a**2 + np.sin(a) + 1
c = UnivariateSpline(a, b)
d = c(np.arange(2.1, 3, 0.1))
print(d)
print()

a = np.arange(10)
b = a**2 + np.sin(a) + 1
c = Rbf(a, b)
d = c(np.arange(2.1, 3, 0.1))
print(d)