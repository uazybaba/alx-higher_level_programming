#!/usr/bin/python3
#Print a square

def print_square(size):
    """This function prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
