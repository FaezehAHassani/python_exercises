 # classes and modules

import mystuff
mystuff.apple()
print(mystuff.tangerine)

# define a class and call it with object
class Mystuff(object):

    def __init__(self):  # remember use double _ before and after init
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = Mystuff()
thing.apple()
print(thing.tangerine)

# another example of class
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Happy birthday to you",
                        "I don't want to get sued",
                        "So I'll stop right there!"])

bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells!"])

happy_birthday.sing_me_a_song()

print(happy_birthday.lyrics) # returns ['Happy birthday to you', "I don't eant to get sued", "so I'll stop rigth there!"]

bulls_on_parade.sing_me_a_song()
