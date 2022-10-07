import os
os.system("cls")

fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a)
print()

fruits = ["apple", "banana", "cherry"]
(a, b, c) = fruits
print(a)
print()

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print()

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

fruits = ("apple", "banana", "cherry", "apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()