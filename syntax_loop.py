# list and loop

the_count = [ 1, 2, 3, 4, 5]  # making a list
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
netted_list = [[1, 2, 3], ['me', 'you', 'them']] # make a list in a list

# for-loop

for number in the_count:   # basically putting "the_count" contents in variable "number"
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type {fruit}")

for i in change:
    print(f"I got {i}")

for item in netted_list:
    print(f"{item} shows how to list in a list.")  # this will return: [1, 2, 3] shows how to list in a list.
                                                                     # ['me', 'you', 'them'] shows how to list in a list.

elements = []  # make an empty list

for i in range(0, 6):  # put the numbers in the range of 0 t0 6 inside variable "i"
    print(f"Adding {i} to the list.")
    elements.append(i) # append will add contents in "i" to the empty list "elements"

for i in elements:
    print(f"Element was: {i}")

digits = []

for digits in range(0, 6):
    print(f" Directly add {digits} to empty list")
