#!/usr/bin/python3

class Node:
    """
    Node class for a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node with the given data and an optional next_node.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """
        Get the data of the Node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the next Node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list with a head node set to None.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node wth the given val into the correct sorted position in the list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the singly linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
