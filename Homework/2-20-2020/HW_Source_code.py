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
rmoi = 0

while (restart.lower() == 'y'):
    print("Thank you for choosing this program to help you with Rectangular Moment of Inertia!")
    print("Please choose from the following options:")
    print("Type 'I' for I-beam")
    print("Type 'R' for rectangular beam")
    print("Type 'C' for cylindrical beam")
    beam = input("")

    if (beam.lower() == 'i' or beam.lower() == 'r'):
        b = eval(input("Please enter the value for 'b' in inches: "))
        while (b <= 0):
            b = eval(input("Invalid. Please enter the value for 'b' in inches: "))
            
        h = eval(input("Please enter the value for 'h' in inches: "))
        while (h <= 0):
            h = eval(input("Invalid. Please enter the value for 'h' in inches: "))

        if (beam.lower() == 'i'):
            B = eval(input("Please enter the value for 'B' in inches: "))
            while (B <= 0):
                B = eval(input("Invalid. Please enter the value for 'B' in inches: "))

            H = eval(input("Please enter the value for 'H' in inches: "))
            while (H <= 0):
                H = eval(input("Invalid. Please enter the value for 'H' in inches: "))
            rmoi = ((B * (H**3)) - (b * (h**3)))/12
            print("Given b =", b, "inches, h =", h, "inches, B =", B, "inches, and H =", H, "inches,")
            print("The Rectangular Moment of Inertia for this I-beam is", rmoi,)
        else:
            rmoi = (b * (h**3))/12
            print("Given b =", b, "inches and h =", h, "inches,")
            print("The Rectangular Moment of Inertia for this rectangular beam is", rmoi,)
    elif (beam.lower() == 'c'):
        r = eval(input("Please enter the value for r in inches: "))
        while (r <= 0):
            r = eval(input("Invalid. Please enter the value for r in inches: "))
        rmoi = (3.14 * (r**4))/4
        print("Given r =", r, "inches,")
        print("The Rectangular Moment of Inertia of the circular beam is", rmoi)
    
    restart = input("Would you like to try again? <y/n>? ")
