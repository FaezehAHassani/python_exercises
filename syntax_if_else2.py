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
    elif bear == "2"
    print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is better.")
        print("Bear runs away.")
