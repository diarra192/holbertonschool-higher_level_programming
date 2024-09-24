#!/usr/bin/python3

""" That class square define or that has define a square define gooogledvvd
"""


class Square:
""" Thar define square or define gooogle dssssqqqd
"""

    def __init__(self, size=0):
        self.__size = size

    # Property
    @property
    def size(self):
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
