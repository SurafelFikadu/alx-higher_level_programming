#!/usr/bin/python3
"""Create an empty class called square
"""


class square:
    """Instation with optional
    """
    size: def __int___(self, size=0):
        """
                insatation with size
        args:
                size: size of a square
        """
        if size is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ Public instance method
    """
    def area(self):
        """Return th ecurrent square area
        """
        return (self.__size * self.__size)
