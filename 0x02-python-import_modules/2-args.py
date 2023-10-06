#!/usr/bin/python3

# Check if the script is being run as the main program
if __name__ == "__main__":
    import sys
    
    # Get the number of command-line arguments
    argLen = len(sys.argv)
    
    # Check the number of arguments and print the appropriate message
    if argLen == 1:
        print("{} arguments.".format(argLen - 1))
    elif argLen == 2:
        print("{} argument:".format(argLen - 1))
    else:
        print("{} arguments:".format(argLen - 1))
    
    # Loop through the command-line arguments and print each one
    for i in range(1, argLen):
        print("{}: {}".format(i, sys.argv[i]))
