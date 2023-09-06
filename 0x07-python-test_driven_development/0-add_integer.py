#!/usr/bin/python3

def add_integer(a, b=98):
    """Returns int val of sum (a, b).

    Float arguments are typecasted to ints before sum.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
