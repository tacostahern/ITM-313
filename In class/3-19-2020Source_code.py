'''
This program will ask a user to enter any number of double values up to 10
numbers. It will display an error message if the user quits without entering any
numbers, otherwise it will display each number entered and its distance from the
average
Author: Tony Acosta Hernandez
Course: ITM 313
'''

num = eval(input("Please enter any number: "))
l = []

while ((num != -99999) and (len(l) < 11)):
    l.append(num)

if (len(l) == 0):
    print("Error")
else:
    for x in l:
        average += x
    average = average/len(l)

    for x in l:
        print("Entered:", x, "Distance from average:", (x - average))
