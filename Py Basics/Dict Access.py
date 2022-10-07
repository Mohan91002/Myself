import os
os.system("cls")

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
print(a["year"])
print()


a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
print(a.get("year"))
print()

a =    {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
print(a.keys())
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car)
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car.values())
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["color"] = "white"
print(car.items())
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "year" in car:
       print("Year" in car)
else:
       print(False)
print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in car:
       print("model" in car)
else:
       print(False)
print()