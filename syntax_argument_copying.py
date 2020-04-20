# Copying one file to other

from sys import argv
from os.path import exists  # import exists command from os.path library; this returns True if file exists and False if file does not exist

script, from_fle, to_file = argv

print(f"copying from {from_file} to {to_file)}.")

# the below two lines can be replaced by:  indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()
