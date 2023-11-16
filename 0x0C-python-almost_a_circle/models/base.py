#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle

class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    # Private class attribute to keep track of the number of instantiated Bases
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base. If None, a unique ID is assigned.
        """

        # Check if id is provided, if not, generate a unique ID
        if id is not None:
            self.id = id
        else:
            # Increment the class attribute to get a unique ID for the new Base
            Base.__nb_objects += 1
            # Assign the new value to the public instance attribute id
            self.id = Base.__nb_objects

# The provided code defines a base model class with a mechanism to generate unique IDs for instances of the class.
# It includes private class attributes and a constructor to initialize instances with a specified ID or generate a unique one.
# The class can be used as a base for other classes in project 0x0C*.

class YourClassName:
 @staticmethod
def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        # Check if the input list is None or empty
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"  # Return an empty JSON array string

        # Use json.dumps to convert the list of dictionaries to a JSON string
        # json.dumps takes care of the serialization process
        json_string = json.dumps(list_dictionaries)

        return json_string  # Return the JSON string representing the list of dictionaries

@classmethod
def save_to_file(cls, list_objs):
    """Write the JSON serialization of a list of objects to a file.

    Args:
        list_objs (list): A list of inherited Base instances.
    """
    # Generate a filename based on the class name and use JSON extension
    filename = cls.__name__ + ".json"

    # Open the file in write mode
    with open(filename, "w") as jsonfile:
        # Check if the list of objects is None
        if list_objs is None:
            # If the list is None, write an empty list to the file
            jsonfile.write("[]")
        else:
            # Convert each object to a dictionary using the to_dictionary method
            # for each object in the list, creating a list of dictionaries
            list_dicts = [o.to_dictionary() for o in list_objs]

            # Serialize the list of dictionaries to a JSON-formatted string
            json_string = Base.to_json_string(list_dicts)

            # Write the JSON string to the file
            jsonfile.write(json_string)

@staticmethod
def from_json_string(json_string):
    """
    Return the deserialization of a JSON string.

    Args:
        json_string (str): A JSON str representation of a list of dicts.

    Returns:
        If json_string is None or empty - an empty list.
        Otherwise - the Python list represented by json_string.
    """
    # Check if the input json_string is None or an empty list "[]"
    if json_string is None or json_string == "[]":
        # Return an empty list if json_string is None or empty
        return []

    # Use json.loads to convert the JSON string to a Python list
    # Note: Ensure that the 'json' module is imported before using json.loads
    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """Return a class instantiated from a dictionary of attributes.

    Args:
        **dictionary (dict): Key/value pairs of attributes to initialize.
    """
    # Check if the dictionary is not empty
    if dictionary and dictionary != {}:
        # Check if the class is a Rectangle
        if cls.__name__ == "Rectangle":
            # Instantiate a Rectangle with default values (width=1, height=1)
            new = cls(1, 1)
        else:
            # Instantiate a Square with default value (side_length=1)
            new = cls(1)
        
        # Update the instantiated object with values from the dictionary
        new.update(**dictionary)
        
        # Return the instantiated object
        return new

@classmethod
def load_from_file(cls):
    """Return a list of classes instantiated from a file of JSON strings.

    Reads from `<cls.__name__>.json`.

    Returns:
        If the file does not exist - an empty list.
        Otherwise - a list of instantiated classes.
    """
    # Construct the filename based on the class name and the '.json' extension
    filename = str(cls.__name__) + ".json"
    
    try:
        # Try to open the file in read mode
        with open(filename, "r") as jsonfile:
            # Deserialize JSON string and create instances from dictionaries
            # Here, 'Base' is assumed to have a 'from_json_string' method
            # that deserializes a JSON string into a list of dictionaries
            list_dicts = Base.from_json_string(jsonfile.read())
            
            # Create instances of the class using the 'create' method
            # The 'create' method is assumed to be a class method that
            # takes keyword arguments and instantiates the class
            return [cls.create(**d) for d in list_dicts]
    
    except IOError:
        # If the file does not exist, return an empty list
        return []
    
@classmethod
def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        # Generate a filename based on the class name with a ".csv" extension
        filename = cls.__name__ + ".csv"

        # Open the file in write mode with newline="" to ensure consistent line endings
        with open(filename, "w", newline="") as csvfile:
            # Check if the list is None or empty
            if list_objs is None or list_objs == []:
                # If the list is None or empty, write an empty list to the file
                csvfile.write("[]")
            else:
                # Determine fieldnames based on the class type
                if cls.__name__ == "Rectangle":
                    # Fieldnames for the Rectangle class
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    # Fieldnames for other classes (assuming it has 'size' attribute)
                    fieldnames = ["id", "size", "x", "y"]

                # Use csv.DictWriter to write dictionaries to the CSV file
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Iterate over the list of objects and write their dictionaries to the CSV file
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
                      
@classmethod
def load_from_file_csv(cls):
    """Return a list of classes instantiated from a CSV file.

    Reads from `<cls.__name__>.csv`.

    Returns:
        If the file does not exist - an empty list.
        Otherwise - a list of instantiated classes.
    """
    # Construct the filename based on the class name
    filename = cls.__name__ + ".csv"

    try:
        # Try opening the CSV file for reading
        with open(filename, "r", newline="") as csvfile:
            # Determine fieldnames based on class type
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]

            # Use csv.DictReader to read dictionaries from CSV file
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)

            # Convert string values to integers in the dictionaries
            list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]

            # Create instances from dictionaries using the class's create method
            return [cls.create(**d) for d in list_dicts]
    except IOError:
        # If the file does not exist, return an empty list
        return []

class ShapeDrawer:
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        # Create a turtle object
        turt = turtle.Turtle()

        # Set up turtle screen
        turt.screen.bgcolor("#b7312c")  # Set background color
        turt.pensize(3)  # Set pen size
        turt.shape("turtle")  # Set turtle shape

        # Draw Rectangles
        turt.color("#ffffff")  # Set color for rectangles
        for rect in list_rectangles:
            turt.showturtle()  # Make turtle visible
            turt.up()
            turt.goto(rect.x, rect.y)  # Move turtle to the starting position of the rectangle
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()  # Hide turtle after drawing the rectangle

        # Draw Squares
        turt.color("#b5e3d8")  # Set color for squares
        for sq in list_squares:
            turt.showturtle()  # Make turtle visible
            turt.up()
            turt.goto(sq.x, sq.y)  # Move turtle to the starting position of the square
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()  # Hide turtle after drawing the square

        # Close the turtle graphics window on click
        turtle.exitonclick()