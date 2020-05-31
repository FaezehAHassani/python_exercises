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

# load up the words from the downloaded words.txt file
for word in WORD_URL.readlines():  # replaced urlopen(WORDS) with WORD_URL
    WORDS.append(str(word.strip())) # removed , encoding = "utf-8" from here and put it in line 8

def convert(snippet, phrase):
    class_name = [w.capitalize() for w in
        random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.samples(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randit(1,3)
        param_names.append(', '.join(
             random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]
