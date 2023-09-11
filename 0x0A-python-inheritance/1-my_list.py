#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """use sorted printing for the built-in list class"""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
