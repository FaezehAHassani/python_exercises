# Parameters, unpacking, variables

from sys import argv
members, m1, m2, m3, m4, m5 = argv

print(f"names of members are: {m1}, {m2}, {m3}, {m4}, {m5}")
print("first member is:", m1)
print("last member is:", m5)
print(input(f"how old are you {m1}?"))
