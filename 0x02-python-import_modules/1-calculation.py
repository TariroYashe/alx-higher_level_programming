#!/usr/bin/python3
# Import the functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define the variables a and b
a = 10
b = 5

# Call each of the imported functions with a and b
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Print the results, but not more than 4 times as required
print("Result of addition:", result_add)
print("Result of subtraction:", result_sub)
print("Result of multiplication:", result_mul)
print("Result of division:", result_div)
