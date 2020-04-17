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

print("Type the filename again:")
file_again2 = input() # without prompt

txt_again2 = open(file_again2)

print(txt_again2.read())

close(txt)

close(txt_again)

close(txt_again2)
