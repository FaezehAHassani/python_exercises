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
my_list[0] = 0 **returns [0, 2, 3, 4]**
my_list[2:4] = [7, 8]
print(my_list) **returns [0, 2, 7, 8]**

# adding index to the end of list
my_list = [0, 2, 3, 4]
my_list.append (6)
print(my_list) **returns [0, 2, 3, 4, 6]**

# adding several index to the end of list
my_list = [0, 2, 3, 4, 6]
my_list.extend([8, 0, 3])
print(my_list) **returns [0, 2, 3, 4, 6, 8, 0, 3]**

_ex2:_

my_nested_list =[[1 , 3], [9, 0]]

# calling an index in a nested list
my_nested_list =[[1 , 3], [9, 0]]
print(my_nested_list[0][1]) **returns 3**

print(my_nested_list[1][0]) **returns 9**

# using of +
my_nested_list =[[1 , 3], [9, 0]]
print(my_nested_list + [9, 7, 5]) **returns [[1 , 3], [9, 0], 9, 7, 5]**

_ex3:_

# multiple same index
print(["re"] * 3) **returns ['re', 're', 're']
