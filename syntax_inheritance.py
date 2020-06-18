# inheritance

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()   # here calls back to altered in PARENT
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


dad.override()
son.override()

dad.altered()
son.altered()

class Other(object):

    def override(self):
        print("OTHER overide()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        perint("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = child()

son.implicit()
son.override()
son.altered()
