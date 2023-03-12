#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
digit = abs(number % 10)

if digit > 5:
    a = "and is greater than 5"
elif digit == 0:
    a = "and is 0"
else:
    a = "and is less than 6 and not 0"

print(f"Last digit of {number} is {digit} {a}")
