'''
This program will ask the user to enter the weight of a package then calculate
and display the shipping charges based on the following criteria
2 pounds or less : $1.10
Over 2 pounds but no more than 6 pounds : $2.20
Over 6 pounds but no more than 10 pounds : $3.70
Over 10 pounds : $3.80
Author: Tony Acosta Hernandez
Course: ITM 313
'''

pounds = eval(input("Please enter the weight of the package in pounds: "))

if (pounds <= 2):
    charges = pounds * 1.10
elif (pounds > 2) and (pounds <= 6):
    charges = pounds * 2.20
elif (pounds > 6) and (pounds <= 10):
    charges = pounds * 3.7
elif (pounds > 10):
    charges = pounds * 3.8
else:
    print("How do you have a negative number weight.")
    charges = 0

print("The total shipping charge is $%.2f" % (charges))
