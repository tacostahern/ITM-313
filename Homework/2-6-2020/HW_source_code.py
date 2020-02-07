'''
This program will ask the user to select an option from a menu consisting
of water, air, and steel. They will then be asked to enter the distance a
sound wave will travel the selected medium, at which point the program will
display the amount of time it will take.
Author: Tony Acosta Hernandez
Course: ITM 313
'''
print("Medium\tSpeed")
print("Air\t1,100 feet per second")
print("Water\t4,900 fett per second")
print("Steel\t16,400 feet per second")

choice = input("Please enter 'a' for air, 'w' for water, or 's' for steel: ")
if (choice.lower() == "a"):
    speed = 1100
    medium = "air"
elif (choice.lower() == "w"):
    speed = 4900
    medium = "water"
elif(choice.lower() == "s"):
    speed = 16400
    medium = "steel"
else:
    print("Wrong choice, buddy")
    print("Automatically selecting air")
    speed = 1100
    medium = "air"

distance = eval(input("Please enter the distance the sound wave will travel: "))
if (distance < 0):
    print("Wrong again")
    print("Automatically choosing 0")
    distance = 0

time = distance / speed

print("In the medium", medium, "the speed of sound is", speed, "feet per second")
print("Given the distance", distance, "feet, the time taken to travel is %.4f" % (time), "seconds")
    
