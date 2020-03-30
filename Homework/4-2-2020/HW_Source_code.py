'''
This program will read the contents of 2 files: data1.txt and data2.txt. It will
then calculate the sum, mean, and median of all numbers stored in each file and
print them out
Author: Tony Acosta Hernandez
Course: ITM 313
'''
import os, statistics

sum = 0
mean = 0
median = 0

f1 = "data1.txt"

if os.path.isfile(f1):
    infile = open(f1, "r")

    s1 = infile.read()

    num1 = [ eval(x) for x in s1.split() ]
    for x in num1:
        sum += x
    mean = sum/len(num1)
    print("The sum for data1.txt is", sum)
    print("The mean is", mean)
    
else:
    print("data1.txt does not exists")

f2 = "data2.txt"

if os.path.isfile(f2):
    infile = open(f2, "r")

    s2 = infile.read()

    
else:
    print("data2.txt does not exists")
