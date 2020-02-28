'''
This program will have two functions: one for checking if 3 sides of a triangle
are valid and the other for calculating the area of the triangle.
Author: Tony Acosta Hernandez
Course: ITM 313
'''
import math

def isValid(side1, side2, side3):
    if ((side1 + side2) <= side3):
        return False
    elif ((side1 + side3) <= side2):
        return False
    elif ((side2 + side3) <= side1):
        return False
    else:
        return True

def area(side1, side2, side3):
    s = (side1 + side2 + side3)/2
    temp = s * (s - side1) * (s - side2) * (s - side3)
    a = math.sqrt(temp)
    return a

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if (isValid(side1, side2, side3) is not True):
    print("Input invalid!")
else:
    print("The area of the triangle is ", area(side1, side2, side3))
