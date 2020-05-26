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
