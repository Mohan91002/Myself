import os
import pandas as pd
os.system('cls')

df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
print()

df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())
print()

df = pd.read_csv('data.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())
print()

df = pd.read_csv('data.csv')
for x in df.index:
       if df.loc[x, "Duration"] > 120:
              df.loc[x, "Duration"] = 120
print(df.to_string())
print()

df = pd.read_csv('data.csv')
for x in df.index:
       if df.loc[x, "Duration"] > 120:
              df.drop(x, inplace = True)
print(df.to_string())