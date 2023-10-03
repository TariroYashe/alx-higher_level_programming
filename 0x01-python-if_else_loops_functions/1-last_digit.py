#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_num = abs(number) % 10  # Calculate the last digit

if last_num > 5:
    message = "greater than 5"
elif last_num == 0:
    message = "0"
else:
    message = "less than 6 and not 0"

print(f"Last digit of {number} is {last_num} and is {message}")