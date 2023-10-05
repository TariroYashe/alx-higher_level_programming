#!/usr/bin/python3

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define variables a and b on separate lines
a = 10
b = 5

# Call the imported functions using a and b, and print the results
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Print the results without using print more than 4 times
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_sub))
print("{} * {} = {}".format(a, b, result_mul))
print("{} / {} = {}".format(a, b, result_div))
