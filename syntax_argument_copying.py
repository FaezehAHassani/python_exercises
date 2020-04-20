# Copying one file to other

from sys import argv
from os.path import exists  # import exists command from os.path library; this returns True if file exists and False if file does not exist

script, from_file, to_file = argv  # remember to write this when running in terminal: python3.7 syntax_argument_copying.py original.txt destination.txt


print(f"copying from {from_file} to {to_file}.")

# the below two lines can be replaced by:  indata = open(from_file).read() => if you use this, you don't need to do in_file.close()
#indata = open(from_file).read()
in_file = open(from_file) # open from_file
indata = in_file.read()   # read from_fle

print(f"The input file is {len(indata)} bytes long") # len(indata) gives the bytes lenght of data

print(f"Does the output file exist?{exists(to_file)}") # if exists rturns TRUE if not returns false and it creates the new file

print("ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, "w")
out_file.write(indata)  # write whatever read from from_file to out_file

print("alright, all done!")

out_file.close()
in_file.close()
