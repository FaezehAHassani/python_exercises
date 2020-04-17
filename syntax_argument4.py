# Reading seperate saved files

from sys import argv
script, filename = argv

txt = open(filename) # open the file

print(f"Here's your file {filename}:")
print(txt.read())  # read and print the file content

print(txt.close()) # it closed the file and returns None

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
print(txt.close())

print("Type the filename again:")
file_again2 = input() # without prompt

txt_again2 = open(file_again2)

print(txt_again2.read())
print(txt.close())
