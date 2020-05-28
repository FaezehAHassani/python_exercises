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
