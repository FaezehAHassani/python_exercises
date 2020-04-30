# decode a script by using UTF-8 decoding with "strict" error

#import sys
#script, language_file.agrv

def main(language_file):
    line = language_file.readline()
    if line:
       return main(language_file)

def print_line(line, errors):
    #next_lang = line.strip()
    cooked_string = next_lang.decode()
    raw_bytes = cooked_string.encode()
    print(cooked_string, "<==>", raw_bytes)
    #print(cooked_string)

languages = open("languages3.txt")

main(languages) # this is used for making a loop unless if line: returns nothing and this loop is stopped
