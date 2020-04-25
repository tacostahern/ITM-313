'''
The following prograg will be for GUI practice. It will ask the user to enter
their full name, field major, and number of semesters in school. They will also
be asked to enter two numbers. The sum and product of the two numbers will be
calculated. Finally, all input will be printed out into one window box
Author: Tony Acosta Hernandez
Course ITM 313
'''

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

def main():
    name = simpledialog.askstring("Full Name", "Enter your name")
    result = "Your name is: " + name

    fm = simpledialog.askstring("Field Major", "Enter your field major")
    result = result + "\nYour field major is: " + fm

    numSemesters = simpledialog.askstring("Number of Semesters", "Enter your number of semesters")
    result = result + "\nThe number of semesters you have had in school is: " + numSemesters
    
    num1 = simpledialog.askstring("First Number", "Enter a number")
    result = result + "\nThe first number you entered is: " + num1

    num2 = simpledialog.askstring("Second Number", "Enter another number")
    result = result + "\nThe second number you entered is: " + num2

    summ = float(num1) + float(num2)
    product = float(num1) * float(num2)

    result = result + "\nThe sum of the two numbers is: " + str(summ)
    result = result + "\nThe product of the two numbers is: " + str(product)
    
    messagebox.showinfo("Display Results", result)


main()
