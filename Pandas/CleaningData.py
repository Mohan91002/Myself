import os
import pandas as pd
os.system("cls")

# df = pd.read_csv('contacts.csv')
# print(df.to_string())
# print()

# df = pd.read_csv('contacts.csv')
# b = df.dropna()
# print(b.to_string())
# print(b.info())
# print()

# df = pd.read_csv('contacts.csv')
# df.dropna(inplace = True)
# print(df.to_string())
# print()

# df = pd.read_csv('contacts.csv')
# df.fillna(130, inplace = True)
# print(df)

# df = pd.read_csv('contacts.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())
# print()

# df = pd.read_csv('contacts.csv')
# df["E-Mail"].fillna(130, inplace = True)
# print(df)
# print()

# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
# print(df)
# print()

df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df)
print()

# df = pd.read_csv('data.csv')
# x = df["Calories"].mode()
# df["Calories"].fillna(x, inplace = True)
# print(df)