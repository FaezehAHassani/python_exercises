# Functions and files

from sys import agrv

script, input_file = agrv

def print_all(f):
    print(f.read())

def rewind(f):  # rewind is like rewinding a tape/ go back to the tape beginning
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count, f.readline())

current_file = open(input_file)

print("Let's first print the whole file:\n")
print_all(current_file)

print("Let's rewind the file")
rewind(current_file)
