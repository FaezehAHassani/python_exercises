# encode a script by using UTF-8 encoding with "strict" error
# in terminal type: python3.7 syntax_encoding.py utf-8 strict
# for other encoding try: python3.7 syntax_encoding.py utf-16 strict OR python3.7 syntax_encoding.py big5 strict

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:    # using an if statement, if we read a line and it returns something it means this is not the last line, print the contents and go to the next line
       print_line(line, encoding, errors)
       return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    print(raw_bytes, "<==>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error) # this is used for making a loop unless if line: returns nothing and this loop is stopped
