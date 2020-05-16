# list

https://www.programiz.com/python-programming/list  up to Python List Methods

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

# insert an index in the slices of a my_list: e.g. for the my_nested_list = [[1 , 3], [9, 0], 9, 7, 5] => the slices numbers are 0 1 2 3 4
my_nested_list = [[1 , 3], [9, 0], 9, 7, 5]

my_nested_list.insert(1,3)   **=> put 3 in the slice 1**
print(my_nested_list) **returns [[1 , 3], 3, [9, 0], 9, 7, 5]**

my_nested_list = [[1 , 3], 3, [9, 0], 9, 7, 5]
my_nested_list[2:2] = [5, 7]  **=> put 5, 7 in the slice 2**
print(my_nested_list) **returns [[1 , 3], 3, 5, 7, [9, 0], 9, 7, 5]**

# delete one index or multiple index from a list
my_nested_list = [[1 , 3], 3, 5, 7, [9, 0], 9, 7, 5]
del my_nested_list[1]
print(my_nested_list) **returns [[1 , 3], 5, 7, [9, 0], 9, 7, 5]**
del my_nested_list[3:6]
print(my_nested_list) **returns [[1 , 3], 5, 7, 5]**
del my_nested_list
print(my_nested_list) **gives an error that name 'my_nested_list' is not defined**

my_nested_list = [[1 , 3], 3, 5, 7, [9, 0], 9, 7, 5]
my_nested_list.remove([1,3])
print(my_nested_list) **returns [3, 5, 7, [9, 0], 9, 7, 5]]**
my_nested_list.pop(1)
print(my_nested_list) **returns [3, 7, [9, 0], 9, 7, 5]]**
my_nested_list.pop() => pop() deletes the last index
print(my_nested_list) **returns [3, 7, [9, 0], 9, 7]]**
my_nested_list.clear()
print(my_nested_list) **returns []**

# delete by using slices
my_nested_list = [[1 , 3], 3, 5, 7, [9, 0], 9, 7, 5]
my_nested_list[2:3] = []
print(my_nested_list) **returns [[1 , 3], 3, 7, [9, 0], 9, 7, 5]**
my_nested_list[2:5] = []
print(my_nested_list) **returns [[1 , 3], 3, 7, 5]**

_ex3:_

# multiple same index
print(["re"] * 3) **returns ['re', 're', 're']

# Summary of commands for List

- append() - Add an element to the end of the list
- extend() - Add all elements of a list to the another list
- insert() - Insert an item at the defined index
- remove() - Removes an item from the list
- pop() - Removes and returns an element at the given index
- clear() - Removes all items from the list
- index() - Returns the index of the first matched item
- count() - Returns the count of the number of items passed as an argument
- sort() - Sort items in a list in ascending order
- reverse() - Reverse the order of items in the list
- copy() - Returns a shallow copy of the list

_ex4:_
my_list = [8, 0, 2, 10, 6, 8, 4, 7]

print(my_list.index(8)) **returns 0 that is the index number for first 8**

my_list.sort()
print(my_list) **returns [0, 2, 4, 6, 7, 8, 8, 10]**

my_list.reverse()
print(my_list) **returns [10, 8, 8, 7, 6, 4, 2, 0]**

_ex5:_
pow2 = [2 ** x for x in range(10)] comment: 2 ** x is 2^x
print(pow2)  **returns [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]**

**is equivalent to:**

pow2 = []
for x in range(10):
   pow2.append(2 ** x)
pow2 **returns [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]**

_ex6:_
pow2 = [2 ** x for x in range(10) if x > 5]
pow2 **returns [64, 128, 256, 512]**

_ex7:_
odd = [x for x in range(20) if x % 2 == 1]
odd **returns [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]**

_ey8:_
add_value = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(add_value) **returns ['Python Language', 'Python Programming', 'C Language', 'C Programming']**
