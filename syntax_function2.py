# Functions and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses and {boxes_of_crackers} boxes of crackers!")
    print("Girl that's enough for a party!")
    print("Get a blanket for the picnic party\n")

print("Let's give numbers to the function")
cheese_and_crackers(20, 40)

print("Let's give variables to the function")
amount_of_cheese = 10
amount_of_crackers = 100
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do maths for a function values")
cheese_and_crackers(10 + 20, 10 / 2)

print("We can even combine variables and numbers for a function values")
cheese_and_crackers(amount_of_cheese + (100 / 3), amount_of_crackers - (30 * 2))

def full_name(first_name, last_name):
    print(f"This is your first name: {first_name}.\n")
    print(f"This is your last name: {last_name}.\n")
    print("Your complete name is:")

surname = "liam"
family = "nelson"
full_name(surname, family)

print(input("Your title:"))

def title_full_name(title, complete_name):
    print(f"Your title ({title}) is added to your {complete_name}")
    complete_name_with_title = title_full_name(title, complete_name)

print(f"Your full name with title is: {complete_name_with_title}")
