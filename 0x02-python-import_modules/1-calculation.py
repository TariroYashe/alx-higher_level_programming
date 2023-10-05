#!/usr/bin/python3

# Import specific functions from the 'calculator_1' module
from calculator_1 import add, sub, mul, div

# Define variables 'a' and 'b' with values 10 and 5
a = 10
b = 5

# Perform the mathematical operations and print the results
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Print the results
print(f"Addition: {a} + {b} = {result_add}")
print(f"Subtraction: {a} - {b} = {result_sub}")
print(f"Multiplication: {a} * {b} = {result_mul}")
print(f"Division: {a} / {b} = {result_div}")
