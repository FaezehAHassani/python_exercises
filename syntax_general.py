#### various types of print commands
print("Hello World!")
print("Hello Again") # is used for commenting
print("I like typing this")
print("This is fun")
print('Yay! Printing')
print("I'd much rather you 'not'")
print('I "said" do not touch this')

#### to add calculation to print command
print("my pen", 3 + 5 / 2, 5 > 2, 6 <= 12 / 2) # returns: my pen 5.5 True True; note / and * was done first then + and -

### % is the remainder division on integers
print(4 % 2) # means divide 2 to groups of 4 that is impossible so returns 0

#### assign a value to a variable
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
average_passengers_per_car = passengers / cars_driven
print("we need to put about", average_passengers_per_car, "in each car")

#### format a string with defined variables
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

#### formatting examples
formatter = "{} {}"
print(formatter.format(1, 2, 3, 4)) # format uses the formatter style and returns: 1 2

formatter = "{} {} {} {}"  # returns: I am experiencing new languages new life new passion
print(formatter.format(
    "I am experiencing",
    "new languages",
    "new life",
    "new passion"
))

#### introducing a list of strings
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # \n will print the afterward string in the next line
print("here is a list of the days in a week:   ", days) # the spaces will be printed exactly; returns: here is a list of the days in a week:    Mon Tue Wed Thu Fri Sat Sun
print("here is a list of months:              ", months)
print("""
1
2
hi
3
today is Monday
""")  # """ allows putting several strings in multiple lines, you cannot comment exactly after """ line, returns: each string in a seperate line; you may use ''' instead of """

#### escape double/single quote inside a string, various ways of using """
print("I am 6'2\" tall") # returns: I am 6'2" tall

var1 = "\tI'm tired" # \t introduces a tab
var2 = """
grocery list:\n\t$tomato\n\t$egg\n\t$onion
"""
print(var1, var2)

print("\bI'm you") # \a is to call ASCII BEL to give a bip sound when printing: I'm you

# asking questions
print("how old are you?", end='') # end='' don't let parser go to the next line
age = input() # it will wait until you enter a vlaue for your age
print("how tall are you?" , end='')
height = input()
print("what is your weight?", end='')
weight = input()
print(f"So, you are {age} old, {height} tall and {weight} heavy")

x = int(input()) # this command will get a val;ue from you and convert it to an integer so you can do math on the value

x = input("what is your name:") # entered faezeh
print(f"Hello" + "." * 10 + x) # returns: Hello..........faezeh

# equivalent for using end='' in asking questions in above commands
age = input("how old are you? ")
print(f"if you are {age} old, you are still young")
