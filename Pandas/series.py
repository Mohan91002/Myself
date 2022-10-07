import os
import pandas as pd
os.system("cls")

a = [1, 7, 2]
var = pd.Series(a)
print(var)
print()
print(var[0])
print()

a = [1, 7, 2]
var = pd.Series(a, index = ["x", "y", "z"])
print(var)
print()
print(var["z"])
print()

calories =    {
                     "day1": 420, 
                     "day2": 380, 
                     "day3": 390
              }
myvar = pd.Series(calories)
print(myvar)
print()

calories =    {
                     "day1": 420, 
                     "day2": 380, 
                     "day3": 390
              }
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
print()

data =        {
                     "calories": [420, 380, 390],
                     "duration": [50, 40, 45]
              }
myvar = pd.DataFrame(data)
print(myvar)