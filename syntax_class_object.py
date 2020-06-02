# class A(B) => class A is-a B (object)
# class A(B):   => class A is-a B and has-a __init__ that takes self and C params
#    def __init__(self, C) => C is called attribute

class Animal(object):
    pass

# class Dog is-a Animal that takes __init__ with self and name params, set name attribute to name
class Dog(Animal):
    def __init__(self, name):
        self.name = name
