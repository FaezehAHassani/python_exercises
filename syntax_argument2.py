# Parameters, unpacking, variables

from sys import argv   # calling an import to add sys module (library) from python; agrv stands for argument variable and it hold the arguments you pass to Python script
script, first, second, third, fourth = argv # this command take whatever in agrv, unpack it, and assign it to the variables on the left in order

print("the script called:", script)
print("your first varaiable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)
print("your fourth variable is", fourth)


# example 2
from sys import argv
members, m1, m2, m3, m4, m5 = argv

print(f"names of members are: {m1}, {m2}, {m3}, {m4}, {m5}")
print("first member is:", m1)
print("last member is:", m5)
print(input(f"how old are you {m1}?"))
