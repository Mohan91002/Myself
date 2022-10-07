import os
import pandas as pd
os.system("cls")

df = pd.read_csv("data.csv")
print(df.head(10))
print()

df = pd.read_json("Data.json")
print(df.head())
print()

df = pd.read_json("Data.json")
print(df.head(-5))
print()

df = pd.read_json("Data.json")
print(df.tail())
print()

df = pd.read_json("Data.json")
print(df.info())