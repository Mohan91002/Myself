import os
os.system("cls")

import json
x =  '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
print()

x =    {
              "name": "John",
              "age": 30,
              "city": "New York"
       }
y = json.dumps(x)
print(y)
print()

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

print(type(json.dumps({"name": "John", "age": 30})))
print(type(json.dumps(["apple", "bananas"])))
print(type(json.dumps(("apple", "bananas"))))
print(type(json.dumps("hello")))
print(type(json.dumps(42)))
print(type(json.dumps(31.76)))
print(type(json.dumps(True)))
print(type(json.dumps(False)))
print(type(json.dumps(None)))
print()

x =    {
              "name": "John",
              "age": 30,
              "married": True,
              "divorced": False,
              "children":   (
                                   "Ann","Billy"
                            ),
              "pets": None,
              "cars":[
                            {"model": "BMW 230", "mpg": 27.5},
                            {"model": "Ford Edge", "mpg": 24.1}
                     ]
       }      
print(json.dumps(x))
print()

x =    {
              "name": "John",
              "age": 30,
              "married": True,
              "divorced": False,
              "children":   (
                                   "Ann","Billy"
                            ),
              "pets": None,
              "cars":[
                            {"model": "BMW 230", "mpg": 27.5},
                            {"model": "Ford Edge", "mpg": 24.1}
                     ]
       }      
print(json.dumps(x,indent=7))
print()

x =    {
              "name": "John",
              "age": 30,
              "married": True,
              "divorced": False,
              "children":   (
                                   "Ann","Billy"
                            ),
              "pets": None,
              "cars":[
                            {"model": "BMW 230", "mpg": 27.5},
                            {"model": "Ford Edge", "mpg": 24.1}
                     ]
       }      
print(json.dumps(x,indent=7,separators=(".","=")))
print()

x =    {
              "name": "John",
              "age": 30,
              "married": True,
              "divorced": False,
              "children":   (
                                   "Ann","Billy"
                            ),
              "pets": None,
              "cars":[
                            {"model": "BMW 230", "mpg": 27.5},
                            {"model": "Ford Edge", "mpg": 24.1}
                     ]
       }      
print(json.dumps(x,indent=7,sort_keys=True))
print()

