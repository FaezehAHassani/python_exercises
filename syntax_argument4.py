# Reading seperate saved files

from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())  # read the files

print("Type the filename again:")
file_again = input(">")
