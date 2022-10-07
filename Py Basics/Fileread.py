import os
os.system("cls")

f = open("Step by Step Process.txt", "r")
print(f.read())
print()

print(open("D:\\Tutorials\\Python\\Step by Step Process.txt", "r").read())
print()

print(open("Step by Step Process.txt", "r").read(10))
print()

f = open("Step by Step Process.txt", "r")
print(f.readline())
print()

f = open("Step by Step Process.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print()

f = open("Step by Step Process.txt", "r")
for x in f:
       print(x)
print()

f = open("Step by Step Process.txt", "r")
print(f.readline())
f.close()