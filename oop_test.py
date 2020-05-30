# a reading test

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.text"
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
