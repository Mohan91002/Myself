import os
import pandas as pd
os.system("cls")

df = pd.read_csv("contacts.csv")
print(df.to_string())
print()

df = pd.read_csv('contacts.csv')
print(df.to_string()) 
print()
print(df.loc[0])
print()

print(pd.options.display.max_rows) 
print()

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)