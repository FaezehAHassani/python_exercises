# Prompting and passing

from sys import argv
script, user_name = argv
prompt = '>' # you can enter whatever here that later will be used

print(f"Hi {user_name}, I'm {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What type of computer you have {user_name}?")
computer = input(prompt)

print(f"""
Alright, you said {likes} about liking me.
You live in {lives}. Not sure where is {lives} though?!
And you have a {computer} computer. Nice.
""")
