#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = - number
    if number > 9:
        print("{}".format(number % 10), end="")
    else:
        print("{}".format(number), end="")
    return (number % 10)
