import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
from scipy import stats
from sklearn.metrics import r2_score
os.system("cls")

# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
# plt.scatter(x, y)
# plt.show()
# print()

# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
# train_x = x[:80]
# train_y = y[:80]
# test_x = x[80:]
# test_y = y[80:]
# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
# myline = np.linspace(0, 6, 100)
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# print()

# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
# train_x = x[:80]
# train_y = y[:80]
# test_x = x[80:]
# test_y = y[80:]
# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
# r2 = r2_score(train_y, mymodel(train_x))
# print(r2)
# print()

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
r2 = r2_score(test_y, mymodel(test_x))
print(r2)