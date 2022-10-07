import os
import pandas as pd
os.system("cls")

data   =        {
                     "calories": [420, 380, 390],
                     "duration": [50, 40, 45]
              }
df     =      pd.DataFrame(data)
print(df)
print()

print(df.loc[0])
print()

print(df.loc[[0, 1]])
print()

data   =        {
                     "calories": [420, 380, 390],
                     "duration": [50, 40, 45]
              }
df     =      pd.DataFrame(data, index = ["x", "y", "z"])
print(df)
print()

data   =        {
                     "calories": [420, 380, 390],
                     "duration": [50, 40, 45]
              }
df     =      pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day1"])
print()

df     =      pd.read_csv("data.csv")
print(df)