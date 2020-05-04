def break_words(stuff):
    """This function will bvreak up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints last worf after popping it off."""
    word = word.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentenceand returns the sorted words."""
    words = break_words(sentence)
    return sort_words(sentence)
