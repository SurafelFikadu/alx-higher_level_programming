#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        return (number % 10)
    else:
        return (abs(number) % 10) * (-1)