# list

https://www.programiz.com/python-programming/list

_ex1:_

my_list = [1, 2, 3, 4]

# calling a selected index
my_list = [1, 2, 3, 4]
my_list[0] **returns 1**

# calling a negative index
my_list = [1, 2, 3, 4]
my_list[-1] and my_list[3] **returns 4**

# printing a set of index
my_list = [1, 2, 3, 4]
print(my_list[0:3]) **returns [1, 2, 3]**

print(my_list[:-3]) **returns [1]**

# replacing an index
my_list = [1, 2, 3, 4]
my_list[0] = 0
print(my_list) **returns [0, 2, 3, 4]**

# adding index to the end of list
my_list = [0, 2, 3, 4]
my_list.append (6)
print(my_list) **returns [0, 2, 3, 4, 6]**

_ex2:_

my_nested_list =[[1 , 3], [9, 0]]

print(my_nested_list[0][1]) **returns 3**

print(my_nested_list[1][0]) **returns 9**
