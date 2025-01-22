#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous_cursor = 0
    sum = 0
    for char in roman_string[::-1]:
        cursor = romans[char]
        if cursor < previous_cursor:
            sum -= cursor
        else:
            sum += cursor
        previous_cursor = cursor
    return sum
