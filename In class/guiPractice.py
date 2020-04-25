import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
root = tk.Tk()
root.withdraw()
answer = True
while (answer):
    name = simpledialog.askstring("Type your full name", "Enter your name")
    result = "Your name is: " + name
    idNumber = simpledialog.askinteger("Input four digit ID number", "Enter ID#")
    result = result + "\n" + "Your ID# is: " + str(idNumber) + "\n"
    cost = simpledialog.askfloat("Input cost per credit hour", "Enter cost per credit")
    result = result + "Cost per credit hour is: " + str(cost) + "\n"
    messagebox.showinfo("Display Results", result)
    answer = messagebox.askyesno("Ask Again", "Do you want to re-type the input")
