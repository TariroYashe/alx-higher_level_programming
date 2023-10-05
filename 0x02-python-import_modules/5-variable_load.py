#!/usr/bin/python3
import importlib.util

# Specify the file path and module name
file_path = 'variable_load_5.py'
module_name = 'variable_load_5'

# Load the module
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Access and print the variable 'a' from the loaded module
print(module.a)
