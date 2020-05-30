# a reading test

import random
from urllib.request import urlopen
import sys

#WORD_URL = "http://learncodethehardway.org/words.text" this url gives an error
WORD_URL = open("words.txt", encoding = "utf-8")
WORDS = []

PHRASES = {
"class %%%(%%%): ":
 "Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef__init__(self, ***)":
 "class %%% has-a __init__ that takes self and *** params.",
"class %%%(object):\n\tdef ***(self, @@@)":
 "class %%% has-a function *** that takes self and @@@ params.",
"*** = %%%()":
 "set *** to an instance of class %%%",
"***.***()":
 "from *** get the *** function, call it with params self, @@@",
"***.*** = '***'":
 "from *** get the *** attricute and set it to '***'"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the ords from the website
for word in WORD_URL.readlines():  # replaced urlopen(WORDS) with WORD_URL
    WORDS.append(str(word.strip())) # removed , encoding = "utf-8" from here and put it in line 8
