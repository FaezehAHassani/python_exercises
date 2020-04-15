# Prompting and passing

from sys import argv
script, user_name1, user_name2, user_name3 = argv
prompt = '>' # you can enter whatever here that later will be used

print(f"Hi {user_name1}, I'm {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name1}?")
likes = input(prompt)

print(f"Where do you live {user_name1}?")
lives = input(prompt)

print(f"What type of computer you have {user_name1}?")
computer = input(prompt)

print(f"""
Alright, you said {likes} about liking me.
You live in {lives}. Not sure where is {lives} though?!
And you have a {computer} computer. Nice.
""")

print(f"Hi {user_name2}. I was talking to {user_name1}")
print(f"{user_name1} lives in {lives}.")
print(f"Where do you live {user_name2}?")
lives2 = input(prompt)

print(f"Hi, {user_name3}. {user_name1} lives in {lives}, while {user_name2} lives in {lives2}. What about you, where do you live?")
lives3 = input(prompt)

print(f"Nice, you all live in {lives}!")
