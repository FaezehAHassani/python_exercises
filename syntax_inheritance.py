# inheritance

class Parent(object):

    def override(self):
        print("PARENT override()")

class child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
