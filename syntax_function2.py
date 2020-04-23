# Functions

# define a function named "print_two" that gets two arguments: "Zed", "Shaw" and returnts arg1: Zed, arg2: Shaw
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two("Zed", "Shaw")

# define a function named "print_two_again" that gets two arguments: "Zed", "Shaw" and returnts arg1: Zed, arg2: Shaw
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two_again("Zed", "Shaw")

# define a function named "print_one" that gets one argument: "First!" and returnts arg1: First!
def print_one(arg1):
    print(f"arg1: {arg1}")
print_one("First!")

# define a function named "print_none" that gets nothing and returnts arg1: I got nothin'.
def print_none():
    print("I git nothin'.")
print_none()
