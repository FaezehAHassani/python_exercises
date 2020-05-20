# branches and functions

from sys import exit

# Importent note: first define a few functions but they are not called untill reaching the final line of start()
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("<")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
