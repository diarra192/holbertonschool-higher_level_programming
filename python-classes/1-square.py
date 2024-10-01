#!/usr/bin/python3

"""class defin a square"""


class Square:
    """Class Square that defines a square object."""

    def __init__(self, size):
        """Initialize method that stores the size of the square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

