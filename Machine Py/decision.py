import matplotlib.image as pltimg
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
from scipy import stats
from sklearn.metrics import r2_score
os.system("cls")


df = pandas.read_csv("cars.csv")
print(df)