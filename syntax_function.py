# Functions

# define a function named "print_two" that gets two arguments: "Zed", "Shaw" and returnts arg1: Zed, arg2: Shaw
def print_two(*args): # this will ask for two arguments from your
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two("Zed", "Shaw")

# define a function named "print_two_again" that gets two arguments: "Zed", "Shaw" and returnts arg1: Zed, arg2: Shaw
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two_again("Zed", "Shaw")
