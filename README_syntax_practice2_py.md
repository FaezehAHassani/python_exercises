# README file for running functions defined in syntax_practice2.py file through terminal

In terminal type python3.7 then write line mentioned at each prompt. The returned lines are shown after each line
>>> import syntax_practice2   ===> instead of this line you can type >>> from syntax_practice2 import * ===> Then in all the next lines remove **syntax_practice2.**
>>> sentence = "All good things come to those who wait."
>>> words = syntax_practice2.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = syntax_practice2.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> syntax_practice2.print_first_word(words)
All
>>> syntax_practice2.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> syntax_practice2.print_first_word(sorted_words)
All
>>> syntax_practice2.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = syntax_practice2.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> syntax_practice2.print_first_and_last(sentence)
All
wait.
>>> syntax_practice2.print_first_and_last_sorted(sentence)
All
who
>>>

# the descriptions wrote within """ for each function is called documentation lines. These line make a sort of help document for the function that can be called later. for instance for the syntax_practice2 file we can do as below:
- run python3.7
>>> import syntax_practice2
>>> help(syntax_practice2.break_words)
This returns:
Help on function break_words in module syntax_practice2:

break_words(stuff)
    This function will break up words for us.

- alternatively to the above you can use:
>>> from syntax_practice2 import *
>>> help(break_words)
This returns:

break_words(stuff)
    This function will break up words for us.
