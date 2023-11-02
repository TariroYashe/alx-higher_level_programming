#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    :param first_name: The first name to be printed.
    :param last_name: The last name to be printed (optional).
    :type first_name: str
    :type last_name: str
    :return: None
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        print("My name is {} {}.".format(first_name, last_name))
    else:
        print("My name is {}.".format(first_name))

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)