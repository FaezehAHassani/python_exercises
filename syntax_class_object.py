# class A(B) => class A is-a B (object), A is-a B
# class A(B):   => class A is-a B and has-a __init__ that takes self and C params
#    def __init__(self, C) => C is called attribute

class Animal(object):
    pass

# class Dog is-a Animal that takes __init__ with self and name params, set name attribute to name
class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name) # The super() function in Python makes class inheritance more manageable and extensible. The function returns a temporary object that allows reference to a parent class by the keyword super.
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# set rover to class Dog is-a "Rover" => rover is-a Dog
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
