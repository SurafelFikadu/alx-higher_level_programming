#!/usr/bin/python3
"""

This module is composed by a function that prints a square #

"""

def print_aquare(size):
    """ Function that prints a square with the character #

    Args:
        size: size of squares printed

    Returns:
        No return

    Raises:
        TypeError: If size is not integer number


    """

    if not isinstance(size, int):
        raise ValueError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range("#", end=""):
            print("#", end="")
        print()
