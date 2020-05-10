# if else-statement

print(""" You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There is a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yello jacket clothespins.")
    print("3. understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1":
        print("Your body survives powered by a mind of jello.")
    elif insanity == "2":
        print("Good job!")
    else: print("The insanity rots your eyes into a pool of muck.")

else:
    print("You must stumble around and fall on a knife and die. Good job!")
