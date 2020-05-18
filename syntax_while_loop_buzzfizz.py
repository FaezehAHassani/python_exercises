# print a list of numbers from 1-100, if the number divisible by 15 print FizzBuzz, it divisible by 3 print Fizz, and if divisible by 5 print Buzz

i = 1
numbers = []

while i < 101:
    numbers.append(i)
    i = i + 1

print("The numbers: ")

for num in numbers:
    print(num)

print("Let's go for the FizzBuzz test!")

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
