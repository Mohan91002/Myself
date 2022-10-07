import os
os.system("cls")

e = "mohan kumar satyavarapu"
print(e.capitalize())
print()

e = "mohan kumar satyavarapu"
print(e.casefold())
print()

e = "mohan kumar satyavarapu"
print(e.center(30,"A"))
print()

e = "mohan kumar satyavarapu"
print(e.count("a"))
print()

e = "mohan kumar satyavarapu"
print(type(e.encode()))
print()

e = "mohan kumar satyavarapu"
print(e.encode())
print()

e = "mohan kumar satyavarapu"
print(e.endswith("u"))
print()

e = "mohan\t kumar\t satyavarapu"
print(e.expandtabs(12))
print()

e = "mohan\t kumar\t satyavarapu"
print(e.expandtabs(10))
print()

e = "mohan kumar satyavarapu"
print(e.find("u"))
print()

e = "mohan kumar satyavarapu"
print(e.find("z"))
print()

e = "mohan kumar satyavarapu"
print(e.find("u", 0, 23))
print()

e = "mohan kumar satyavarapu {} {}"
age = 26
dob = "10/05/1995"
print(e.format(age, dob))
print()

e = "mohan kumar satyavarapu {1} {0}"
age = 26
dob = "10/05/1995"
print(e.format(age, dob))
print()

e = "mohan kumar {:<16} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {:>16} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {:^16} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {:=16} satyavarapu"
print(e.format(-26))
print()

e = "mohan kumar {:+} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {:-} satyavarapu"
print(e.format(-26))
print()

e = "mohan kumar {:} satyavarapu"
print(e.format(-26))
print()

e = "mohan kumar {:} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {} satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {: } satyavarapu"
print(e.format(26))
print()

e = "mohan kumar {: } satyavarapu"
print(e.format(-26))
print()

e = "mohan kumar {:,} satyavarapu"
print(e.format(10000))
print()

e = "mohan kumar {:_} satyavarapu"
print(e.format(10000))
print()

e = "mohan kumar {:b} satyavarapu"
print(e.format(65535))
print()

e = "mohan kumar {:c} satyavarapu"
print(e.format(97))
print()

e = "mohan kumar {:d} satyavarapu"
print(e.format(0b111))
print()

e = "mohan kumar {:e} satyavarapu"
print(e.format(111))
print()

e = "mohan kumar {:E} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:f} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:.2f} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:F} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:g} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:G} satyavarapu"
print(e.format(7))
print()

e = "mohan kumar {:o} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:x} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:X} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:n} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:%} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:.0%} satyavarapu"
print(e.format(143))
print()

e = "mohan kumar {:.0%} satyavarapu"
print(e.format(143))
print()

# input stored in variable a.
a = {'x':'John', 'y':'Wick'}
print("{x}'s last name is {y}".format_map(a))
print()

e = "mohan kumar satyavarapu"
print(e.index("u"))
print()

e = "mohan kumar satyavarapu"
print(e.index("u", 0, 22))
print()

e = "mohan12"
print(e.isalnum())
print()

e = "mohan"
print(e.isalpha())
print()

e = "\u0047"
print(e.isdecimal())
print()

e = "1234567890"
print(e.isdigit())
print()

e = "Love_143"
print(e.isidentifier())
print()

e = "mohan kumar satyavarapu"
print(e.islower())
print()

e = "0047"
print(e.isnumeric())
print()

e = "/0047"
print(e.isprintable())
print()

e = "m o h a n k u m a r s a t y a v a r a p     u "
print(e.isspace())
print()

e = "Mohan Kumar Satyavarapu"
print(e.istitle())
print()

e = "MKS"
print(e.isupper())
print()

e = ("Radha","Mohan")
print("@".join(e))
print() 

e = {"name":"Radha","country":"Mohan"}
f = "@"
g = f.join(e)
print(g)
print()

e = "Mohan Kumar Satyavarapu"
print(e.ljust(52,"m"))
print()

e = "mohan kumar satyavarapu"
print(e.islower())
print()

e = " mohan kumar satyavarapu                                         " + "Munna"
print(e.lstrip())
print()

e = "mohan kumar satyavarapu"
f = e.maketrans("m","M")
print(e.translate(f))
print()

e =("mohan kumar")
print(e.partition("munna"))
print()

e = "mohan mohan kumar satyavarapu"
print(e.replace("mohan","Mohan",2))
print()

e = "mohan mohan mohan mohan mohan mohan mohan kumar satyavarapu"
print(e.rfind("mohan"))
print()

e = " Mohan Kumar Satyavarapu"
print(e.rjust(30,"R"))
print()

e = "Mohan Kumar Satyavarapu"
print(e.rindex("r"))
print()

e =("mohan kumar")
print(e.rpartition("munna"))
print()

e =("mohan kumar")
print(e.rsplit())
print()

e = "mohan kumar satyavarapu     " + "munna      "
print(e.rstrip())
print()

e = "mohan kumar satyavarapu"
print(e.split())
print()

e = "mohan kumar satyavarapu \n" + "radha mohan"
print(e.splitlines())
print()

e = "mohan kumar satyavarapu \n" + "radha mohan"
print(e.startswith("o"))
print(e.count("m"))
print()

e = " mohan kumar satyavarapu \n" + " radha mohan "
print(e.strip())
print()

e = "mOhan kumar satyavarapu \n" + "rAdha mohan"
print(e.swapcase())
print()

e = "mohan kumar satyavarapu"
print(e.title())
print()

e = "mohan"
print(e.zfill(10))
print()

e = "mohan"
print(e.isascii())
print()