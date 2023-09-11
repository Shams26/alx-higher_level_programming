#!/usr/bin/python3

class MagicClass:
    pi = 3.14
    def __init__(self, radius=0):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        
        self.__radius = radius

    def area(self):
        return (MagicClass.pi * self.__radius ** 2)

    def circumference(self):
        return (2 * MagicClass.pi * self.__radius)
