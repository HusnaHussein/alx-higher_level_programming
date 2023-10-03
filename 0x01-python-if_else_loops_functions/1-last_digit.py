#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = "Last digit of "
if number < 0:
    last_digit = -last_digit
print("{}{} is {} and is ".format(message, number, last_digit), end='')
if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
else:
    print("is less than 6 and not 0")
