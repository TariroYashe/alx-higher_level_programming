#!/usr/bin/python3

# Check if this script is the main entry point
if __name__ == "__main__":
    # Import necessary modules
    import sys, math
    
    # Initialize a variable to store the result
    result = 0
    
    # Iterate through command-line arguments
    for i in sys.argv:
        # Convert the argument to an integer and add it to the result
        result += int(i)
        
        # Print the current result
        print("{}".format(result))
