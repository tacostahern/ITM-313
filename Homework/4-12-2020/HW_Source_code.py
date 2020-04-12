'''
This program will contain a class called pet, with data attributes for name,
animal type, and age. It will have an __init__ method, and setter and getter
methods for the data attributes.
Author: Tony Acosta Hernandez
Course: ITM 313
'''

class Pet:
    #Construct a pet object
    def __init__(self, name, animal_type, age):
        self.__name, self.__animal_type, self.__age = name, animal_type, age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

name = input("Please enter the name of your pet: ")
#pet1.set_name(name)

animal_type = input("Please enter the type of animal your pet is: ")
#pet1.set_animal_type(animal_type)

age = eval(input("Please enter the age of your pet: "))
#pet1.set_age(age)

pet1 = Pet(name, animal_type, age)

print("Your pet's name is", pet1.get_name())
print("Your pet is a", pet1.get_animal_type())
print("Your pet is", pet1.get_age(), "year old")

