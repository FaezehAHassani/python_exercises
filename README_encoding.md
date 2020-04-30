# strings, bytes, and character encodings
- download languages.txt (https://learnpythonthehardway.org/python3/languages.txt) => right click on the link and click "Save Link Contents As...". Then save it as "languages.txt"
- utf-8, utf-16, and big5 are the types of encodings/**codec** that you can use

# general
- 8 bits of 0/1 makes a byte
- a byte can hold 256 numbers
- American Standard Code for Information Interchange (ASCII) maps a letter to a bit => e.g. letter Z is 90 or 1011010
- you can use a string of a sequence of bytes to shape a word with each letter
- Unicode is a universal encoding that contains 32 bit (= 8 bytes) and can make 2^32 = 4294967295 characters
- To save space better to encode with 8 bits and then move to 16/32 bits if necessary
 - utf-8 (Unicode transformation format 8 bits) do this.
- DBES => decode bytes encode strings

  **in terminal**
  >>> python3.7
  >>> raw_bytes=b'\xd9\x81\xd8\xa7\xd8\xb1\xd8\xb3\xdb\x8c'
  >>> utf_string="فارسی"
  >>> raw_bytes.decode() => returns "فارسی"
  >>> utf_string.encode() => returns b'\xd9\x81\xd8\xa7\xd8\xb1\xd8\xb3\xdb\x8c'
