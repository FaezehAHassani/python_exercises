# Functions for returning something

# defining a few functions:
def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

print("let's do some maths with these functiona!")

age = add(30, 12.5)
height = subtract(90, 190)
weight = multiplying(13.4, 21.88)
iq = divide(30, 0.5)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")
