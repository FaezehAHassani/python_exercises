# Reading and writing files

from sys import argv
script, filename = argv

print(f"We'r going to erase {filename}.")
print("if you don't want that, hit CTRL+C (^C).")
print("if you do want that, hit RETURN.")
input("?")

print("opening the file...")
target = open(filename, "w")

print("truncating the file, Goodbye!")
target.truncate()

print("now I'm going to aske you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it.")
target.close()
