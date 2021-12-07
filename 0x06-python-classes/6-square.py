#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and its size and its
position on the screen, checking if the given values are right, and a setter
and getter methods to set or get them. There's also an area method that returns
the area of the square, another one that handles the print of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
            position (tuple): the coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position
