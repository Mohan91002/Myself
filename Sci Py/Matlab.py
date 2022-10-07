import os
import numpy as np
from scipy import io
os.system("cls")

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
io.savemat('arr.mat', {"vec": arr})
mydata = io.loadmat('arr.mat')
print(mydata)
print()

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
io.savemat('arr.mat', {"vec": arr})
mydata = io.loadmat('arr.mat')
print(mydata['vec'])
print()

mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])