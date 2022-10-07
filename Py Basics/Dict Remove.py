import os
os.system("cls")

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
a.pop("model")
print(a)
print()

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
a.popitem()
print(a)
print()

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
del a["brand"]
print(a)
print()

# a =    {
#               "brand": "Ford",
#               "model": "Mustang",
#               "year": 1964
#        }
# del a
# print(a)
# print()    

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
a.clear()
print(a)
print() 

