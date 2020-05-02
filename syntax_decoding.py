# decode a text file in UTF-8 to strings
#import sys
#script, language_file, error = sys.agrv

def main(language_file):
    line = language_file.readline()
    print(line.encode('utf8'))
    if line:
      return main(language_file)



languages = open("languages2.txt")

main(languages)
