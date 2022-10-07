import os
import pandas as pd
os.system('cls')

df = pd.read_csv('dirtydata.csv')
print(df.duplicated())
print()

df = pd.read_csv('dirtydata.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())