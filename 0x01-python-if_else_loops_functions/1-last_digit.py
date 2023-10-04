#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the absolute value of the number and get its last digit.
digit = abs(number) % 10
# If the original number was negative, make the last digit negative as well.
if number < 0:
    digit = -digit
# Print the original number and its last digit.
print("Last digit of {} is {} and is ".format(number, digit), end="")
# Check if the last digit is greater than 5.
if digit > 5:
    print("greater than 5")
# Check if the last digit is equal to 0.
elif digit == 0:
    print("0")
# If the last digit is not greater than 5 or equal to 0, print this.
else:
    print("less than 6 and not 0")
