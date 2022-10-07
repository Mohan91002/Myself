import os
os.system("cls")

cars = ["BMW","FORD",'Ferrari']
print(len(cars))
print()

cars = ["BMW","FORD",'Ferrari']
for x in cars:
       print(x)
print()

cars = ["BMW","FORD",'Ferrari']
for x in cars:
       print(cars)
print()

cars = ["BMW","FORD",'Ferrari']
print(cars[2])
print()

cars = ["BMW","FORD",'Ferrari']
x = cars[1]
print(x)
print()

cars = ["BMW","FORD",'Ferrari']
cars[1] = "Tata"
print(cars)
print()

cars = ["BMW","FORD",'Ferrari']
cars.append("Tata")
print(cars)
print()

cars = ["BMW","FORD",'Ferrari']
print(cars.append("Tata"))
print(cars)
print()

cars = ['BMW', 'FORD', 'Ferrari', 'Tata']
print(cars.pop())
print()

cars = ['BMW', 'FORD', 'Ferrari', 'Tata']
print(cars.pop(2))
print(cars)
print()

cars = ['BMW', 'FORD', 'Ferrari', 'Tata']
cars.remove("Tata")
print(cars)
print()

cars = ['BMW', 'FORD', "Tata", 'Ferrari']
cars.sort()
print(cars)