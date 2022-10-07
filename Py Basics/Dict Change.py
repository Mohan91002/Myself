import os
os.system("cls")

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
a["year"] = 2021
print(a)
print()

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
a.update({"year" : 2021})
print(a)
print()