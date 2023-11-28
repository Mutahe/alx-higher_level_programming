#!/usr/bin/python3

"""A function that adds two integers"""

def add_integer(a, b=98):
    """Return the sum of integer a and b.
    If a and b are float cast them to integers.
    Raises TypeError if a and b are neither integers or floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
