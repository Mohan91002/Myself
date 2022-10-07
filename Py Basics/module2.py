import os
os.system("cls")

import module
module.greeting("Prami")
print()

import module
print(module.person1)
print()

import module
print(module.person1["age"])
print()

import module as m
print(m.person1["name"])
print()

import platform
print(platform.system())
print()

import platform
print(dir(platform))
print()

import platform
print(dir(platform.python_version))
print()

from module import person1
print(person1)
print()

from module import person1
print(person1["name"])
print()

from module import greeting
x = greeting("Munna")
print(x)