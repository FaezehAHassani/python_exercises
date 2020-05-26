# dictionary: a lisst that not only contains numbers but strings

# example 1
things = ['a', 'b', 'c', 'd']
print(things[1]) # returns b

things[1] = 'z' # replace things[1] with z
print(things[1]) # returns z

things # returns ['a', 'z', 'c', 'd']

# example 2
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2} # remember it uses {} not []
print(stuff['name'])

print(stuff['age'])

print(stuff['height'])

stuff['city'] = 'SF'
print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])

stuff # returns {'name': 'Zed', 'age': 39, 'height': 74, 'city': 'SF', 1: 'Wow', 2: 'Neato'}

del stuff['city']
del stuff[1]
del stuff[2]

stuff # returns {'name': 'Zed', 'age': 39, 'height': 74}

# example 3

# create a mapping of state to abbriviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksoville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)  # returns ----------

print("New York state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do t by using the states then cities dictionary
print('-' * 10)
print("Michigan state has: ", cities[states['Michigan']])
print("Florida state has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):  # here we difned two variable 'abbrev' and 'city'
    print(f"{state} is abbreviated {abbrev}")

# print every city in state abbreviation
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
