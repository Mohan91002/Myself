import os
os.system("cls")

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
       print("YES! We have a match!")
else:
       print("No match")
print()

txt = "The rain in Spain 2022"
x = re.findall("[a-z,A-Z,0-9]", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("\d", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("he..o", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("^hello", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("planet$", txt)
print(x)
print()

txt = "hello planet"
x = re.findall(".*t", txt)
print(x)
print()

txt = "hello planet"
x = re.findall(".+t", txt)
print(x)
print()

txt = "hello planet"
x = re.findall(".?t", txt)
print(x)
print()

txt = "hello planet hello"
x = re.findall("he.{2}o", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("spain|planet", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("\Ahe.*", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("\Ahe..", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("\Ahe*", txt)
print(x)
print()

txt = "hello planet"
x = re.findall("\Ahe..*", txt)
print(x)
print()


txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
if x:
       print("Yes, there is at least one match!")
else:
       print("No match")
print()

txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
if x:
       print("Yes, there is at least one match!")
else:
       print("No match")
print()

txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)
if x:
       print("Yes, there is at least one match!")
else:
       print("No match")
print()

txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
if x:
       print("Yes, there is at least one match!")
else:
       print("No match")
print()

txt = "The rain in Spain 2022"
x = re.findall("\d", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("\D", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("\s", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("\S", txt)
print(x)
print()

txt = "The rain in Spain @ 2022"
x = re.findall("\w", txt)
print(x)
print()

txt = "The rain in Spain_2022"
x = re.findall("\w", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("\W", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("Spain\Z", txt)
if x:
       print("Yes")
else:
       print("No")
print()

txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
if x:
       print("Yes")
else:
       print("No")
print()

txt = "The rain in Spain "
x = re.findall("Spain\Z", txt)
if x:
       print("Yes")
else:
       print("No")
print()

txt = "The rain in Spain 2022"
x = re.findall("[arn]", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("[a-n]", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("[^arn]", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.findall("[123]", txt)
print(x)
print()

txt = "The rain in Spain 2010"
x = re.findall("[0-9]", txt)
print(x)
print()

txt = "The rain in Spain 29:10"
x = re.findall("[0-5][0-9]", txt)
print(x)
print()

txt = "The rain in Spain 2010"
x = re.findall("[a-z,A-Z,0-9]", txt)
print(x)
print()

txt = "The rain in . Spain 2010"
x = re.findall("[.]", txt)
print(x)
print()

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
print()

txt = "The rain in Portugal"
x = re.findall("ai", txt)
print(x)
print()

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
print()

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print()

txt = "The rain in Spain 2022"
x = re.split("\s", txt)
print(x)
print()

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
print()

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
print()

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 1)
print(x)
print()

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print()

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
print()

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())