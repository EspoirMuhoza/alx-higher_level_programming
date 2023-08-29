#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: square size (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: square size (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
