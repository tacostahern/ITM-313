'''
This program will read the contents of 2 files: data1.txt and data2.txt. It will
then calculate the sum, mean, and median of all numbers stored in each file and
print them out
Author: Tony Acosta Hernandez
Course: ITM 313
'''
import os

f1 = "data1.txt"

if os.path.isfile(f1):
    infile = open(f1, "r")

    s = infile.read()
else:
    print("No such file exists")
