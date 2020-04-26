# Functions and files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):  # rewind is like rewinding a tape/ go back to the tape beginning
    f.seek(0) # remmber seek(0) takes us to the first line of the sript

def print_a_line(line_count,f):
    print(line_count, f.readline())

current_file = open(input_file)

print("Let's first print the whole file:\n")
print_all(current_file)

print("Let's rewind the file")
rewind(current_file)

print("Let's print three lines, line by line:")

current_line = 1  # later this may be replaced with a for loop!
print_a_line(current_line, current_file)

# current_line = current_line + 1 instead of this can use below line
current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
