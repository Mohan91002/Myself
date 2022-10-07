import os
os.system("cls")

a =    {
              "Name"        :      "Mohan Kumar Satyavarapu",
              "DOB"         :      10/1995,
              "Address"     :   "Kothapeta"
       }
a.clear()
print(a)
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :   "Kothapeta"
       }
print(a)
print()

a      =      {
                     "Name"        :      "Mohan Kumar",
                     "DOB"         :      "10/05/1995",
                     "Address"     :   "Kothapeta"
              }
radha  = a.copy()
print(radha)
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :   "Kothapeta"
       }
print(a.fromkeys(a))
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :   "Kothapeta"
       }
print(a.fromkeys(a,"Name"))
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :   "Kothapeta"
       }
print(a.get("Address"))
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :   "Kothapeta"
       }
print(a.items())
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :      "Kothapeta"
       }
print(a.keys())
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :      "Kothapeta"
       }
print(a.pop("Address"))
print()

a =    {
              "Name"        :      "Mohan Kumar",
              "DOB"         :      "10/05/1995",
              "Address"     :      "Kothapeta"
       }
print(a.popitem())
print()

car =  {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
x = car.setdefault("color", "White")
print(x)
print()

car =  {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
x = car.setdefault("color", "White")
print(x)
print()

car =  {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
       }
x = car.setdefault("color", "White")
print(x)
print()
print(car.values())
print()