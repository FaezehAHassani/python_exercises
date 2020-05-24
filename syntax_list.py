# doing things to list

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # if I put '' it give an error
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print(more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop() # remove the last index from more_stuff and store it in next_one
    print("Adding: ", next_one)
    stuff.append(next_one) # adds next_one list to the end of stuff list
    print(f"There are {len(stuff)} items now.")
