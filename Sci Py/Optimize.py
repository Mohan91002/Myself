import os
from scipy import constants
from scipy.optimize import root
from scipy.optimize import minimize
from math import cos
os.system("cls")

def eqn(x):
       return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
print()

def eqn(x):
       return x + cos(x)
myroot = root(eqn, 0)
print(myroot)
print()

def eqn(x):
       return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin.x)
print()

def eqn(x):
       return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)