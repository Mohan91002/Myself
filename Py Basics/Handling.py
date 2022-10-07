import os
os.system("cls")

# try:
#        print(x)
# except:
#        print("An exception occurred")
# print()

x = 5
try:
       print(x)
except:
       print("An exception occurred")
print()

try:
       print(x)
except NameError:
       print("Variable x is not defined")
except:
       print("Something else went wrong")
print()

try:
       print("Hello")
except:
       print("Something went wrong")
else:
       print("Nothing went wrong")
print()

try:
       print(x)
except:
       print("Something went wrong")
finally:
       print("The 'try except' is finished")
print()

try:
       f = open("./Step By Step Process.txt")
       try:
              f.write("Lorum Ipsum")
       except:
              print("Something went wrong when writing to the file")
       finally:
              f.close()
except:
       print("Something went wrong when opening the file")
print()

# x = -1
# if x < 0:
#        raise Exception("Sorry, no numbers below zero")
# print()

x = 52
if not type(x) is int:
       raise TypeError("Only integers are allowed")
print(x)

# x = "52"
# if not type(x) is int:
#        raise TypeError("Only integers are allowed")
# print(x)