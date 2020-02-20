'''
This program will calculate the rectangular moment of inertia of one of 3
beams based on the user's choice and input. This program will ask the user to
select between 3 beams: I-beam, rectangular beam, and cylindrical beam.
Depending on the choice, the user will then be asked to enter info as variables
such as B, b, H, h, or r. It will then use this info to calculate and display
the rectangular moment of inertia I.
Author: Tony Acosta Hernandez
Course: ITM 313
'''

restart = 'y' #This will be our variable for restarting the program

while (restart.lower() == 'y'):
    print("Thank you for choosing this program to help you with Rectangular Moment of Inertia!")
    print("Please choose from the following options:")
    print("Type 'I' for I-beam")
    print("Type 'R' for rectangular beam")
    print("Type 'C' for cylindrical beam")
    beam = input("")

    if (beam.lower() == 'i' or beam.lower() == 'r'):
        b = eval(input("Please enter the value for 'b' in inches
    elif (beam.lower() == 'c'):
        pass
    else:
        pass

    restart = input("Would you like to try again? <y/n>? ")
