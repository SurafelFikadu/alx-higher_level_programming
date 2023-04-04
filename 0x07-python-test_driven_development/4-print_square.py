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

    for i in range(size):
        print("#" * size)