
class MyList(list):
    """
    MyList is a custom list class that inherits from the built-in list class.

    Public Methods:
    - print_sorted: Print the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
