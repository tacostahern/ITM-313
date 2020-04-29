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
        return ("Circle has a radius of", self.find_area())
    

class Square:
    def __init__(self, side = 2.5):
        self.__side = side

class Rectangle:
    def __init__(self, length = 2.5, width = 3):
        self.__length, self.__width = length, width

def main():
    Circle circle = new Circle()
    print(circle.display())

main()
