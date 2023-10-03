#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = "Last digit of"
if number < 0:
    last_digit = -last_digit
if number > 5:
    print("{}{} is {} and is greater than 5".format(message, number, last_digit))
elif number == 0:
    print("{}{} is {} and is 0".format(message, number, last_digit))
else:
    print("{}{} is {} and is less than 6 and not 0".format(message, number, last_digit))
