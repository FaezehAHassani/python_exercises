# Reading seperate saved files

from sys import argv
script, filename = argv

txt = open(filename) # open the file

print(f"Here's your file {filename}:")
print(txt.read())  # print the file content

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
