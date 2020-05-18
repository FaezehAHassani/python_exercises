# test for syntax_while_loop_buzzfizz.py

numbers = [2, 15, 9, 6, 5]

j = 0

while j < len(numbers)-1:
    if numbers[j] % 15 == 0:
        print("FizzBuzz")

    if numbers[j] % 5 == 0:
        print("Buzz")
    elif numbers[j] % 3 == 0:
        print("Fizz")
    else:
        print(numbers[j])

    j = j + 1
