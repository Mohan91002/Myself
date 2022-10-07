import os
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe 
from scipy.stats import skew, kurtosis
from scipy.stats import normaltest
os.system("cls")

a = np.random.normal(size=100)
b = np.random.normal(size=100)
c = ttest_ind(a, b)
print(c)
print()

a = np.random.normal(size=100)
b = np.random.normal(size=100)
c = ttest_ind(a, b).pvalue
print(c)
print()

a = np.random.normal(size=100)
b = kstest(a, 'norm')
print(b)
print()

a = np.random.normal(size=100)
b = describe(a)
print(b)
print()

v = np.random.normal(size=100)
print(skew(v))
print()
print(kurtosis(v))
print()

v = np.random.normal(size=100)
print(normaltest(v))