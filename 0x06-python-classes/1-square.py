#!/usr/bin/python3
"""Definition of class square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: square side (1 side).
    """
    def __init__(self, size):
        """Creates new instances of square (1 side).

        Args:
            size: square size.
        """
        self.__size = size
