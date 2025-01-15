#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last = abs(number) % 10
if Last > 5:
    print(f"Last digit of {number} is {Last} and is greater than 5")
elif Last == 0:
    print(f"Last digit of {number} is {Last} and is 0")
else:
    print(f"Last digit of {number} is {Last} and is less than 6 and not 0")
