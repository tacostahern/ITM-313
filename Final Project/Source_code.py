'''
This is my final project for Python
Author: Tony Acosta Hernandez
Course ITM 313
'''

import math

class Circle:
    def __init__(self, radius = 2):
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def find_area(self):
        return math.pi * (self.__radius ** 2)

    def display(self):
        return "Circle has an area of %.2f" % (self.find_area())
    

class Square:
    def __init__(self, side = 2.5):
        self.__side = side

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def find_area(self):
        return self.__side ** 2

    def display(self):
        return "Square has an area of %.2f" % (self.find_area())

class Rectangle:
    def __init__(self, length = 2.5, width = 3):
        self.__length, self.__width = length, width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def find_area(self):
        return self.__length * self.__width

    def display(self):
        return "Rectangle has an area of %.2f" % (self.find_area())

def main():
    circle = Circle()
    print(circle.display())

    square = Square()
    print(square.display())

    rectangle = Rectangle()
    print(rectangle.display())

main()
