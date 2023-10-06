#!/usr/bin/python3

# Check if this script is being run as the main program
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    
    # Import the 'hidden_4' module
    import hidden_4

    # Get a list of all names defined in the 'hidden_4' module
    names = dir(hidden_4)
    
    # Iterate through the names and print those that do not start with "__"
    for name in names:
        if name[:2] != "__":
            print(name)
