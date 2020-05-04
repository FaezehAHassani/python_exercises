# README file for running functions defined in syntax_practice2.py file through terminal

In terminal type python3.7 then write line mentioned at each prompt. The returned lines are shown after each line
>>> import syntax_practice2
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
