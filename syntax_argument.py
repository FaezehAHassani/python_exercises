# Parameters, unpacking, variables

from sys import argv   # calling an import to add sys module (library) from python; agrv stands for argument variable and it hold the arguments you pass to Python script
script, first, second, third, fourth = argv # this command take whatever in agrv, unpack it, and assign it to the variables on the left in order

print("the script called:", script)
print("your first varaiable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)
print("your fourth variable is", fourth)
