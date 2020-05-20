# branches and functions

from sys import exit

# Importent note: first define a few functions but they are not called untill reaching the final line of start()
def gold_room():
    print("This room is full of gold. How much do you take?")
    print("You can select any number")

    choice = input("> ")
    if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)  # this will exit the .py script
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("Your choices are: take honey/ taunt bear")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from  the door.")
            print("You can go through it now.")
            print("Remember to type: open door, otherwise you will be standing there forever")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see th great Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print("Your choices are: flee/ head")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)  # this will exit the .py script

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("Your choices are left/ right")
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
