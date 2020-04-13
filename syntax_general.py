# various types of print commands
print("Hello World!")
print("Hello Again") # is used for commenting
print("I like typing this")
print("This is fun")
print('Yay! Printing')
print("I'd much rather you 'not'")
print('I "said" do not touch this')

# to add calculation to print command
print("my pen", 3 + 5 / 2, 5 > 2, 6 <= 12 / 2) # returns: my pen 5.5 True True; note / and * was done first then + and -

# % is the remainder division on integers
print(4 % 2) # means divide 2 to groups of 4 that is impossible so returns 0

# assign a value to a variable
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
average_passengers_per_car = passengers / cars_driven
print("we need to put about", average_passengers_per_car, "in each car")

# format a string with defined variables
my_name = 'Alex' # '' or "" can both be used for string
my_degree = 'PhD'
my_age = 30
my_weigth = 60
my_height = 200
total = my_age + my_height + my_weigth
print(f"If I have a {my_degree}, I have money. Add {my_age}, {my_weigth}, {my_height} and tell me {total}.") # f format the string; {} to bring a previously defined variable

types_of_people = 10
x = f"There are {types_of_people} types of peaple."
binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"
print(x)
print(y)
print(f"if I said {x}")
print(f"I also said '{y}'")
hilarious = False # don't type FALSE
print("isn't that joke funny?! {}".format(hilarious))
#a = hilarious  this variable introduction is wrong even hilarious was poreviously defined, we cannot have variable on both side, one side should be integer ro sting
print(x + y)

print("I have", "." * 3, "eggs?") # returns I have ... eggs?
end1 = "3"
end2 = "eggs"
print(end1 + ' ' + end2) # 3 eggs

formatter = "{} {}"
print(formatter.format(1, 2, 3, 4)) # format uses the formatter style and returns: 1 2

formatter = "{} {} {} {}"  # returns: I am experiencing new languages new life new passion
print(formatter.format(
    "I am experiencing",
    "new languages",
    "new life",
    "new passion"
))
