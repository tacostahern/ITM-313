'''
This program will read the contents of 2 files: data1.txt and data2.txt. It will
then calculate the sum, mean, and median of all numbers stored in each file and
print them out
Author: Tony Acosta Hernandez
Course: ITM 313
'''
import os, statistics

sum1 = 0
mean1 = 0

sum2 = 0
mean2 = 0

f1 = "data1.txt"

if os.path.isfile(f1):
    infile = open(f1, "r")

    s1 = infile.read()

    num1 = [ eval(x) for x in s1.split() ]
    for x in num1:
        sum1 += x
    mean1 = sum1/len(num1)
    print("The sum for data1.txt is", sum1)
    print("The mean is", mean1)
    print("The median is", (statistics.median(num1)))
    print("The smallest value is", min(num1))
    print("The largest value is", max(num1))
    print("Total numbers read is", len(num1))
else:
    print("data1.txt does not exists")

f2 = "data2.txt"

if os.path.isfile(f2):
    infile = open(f2, "r")

    s2 = infile.read()

    num2 = [ eval(x) for x in s2.split() ]
    for x in num2:
        sum2 += x
    mean2 = sum2/len(num2)
    print("The sum for data2.txt is", sum2)
    print("The mean is", mean2)
    print("The median is", (statistics.median(num2)))
    print("The smallest value is", min(num2))
    print("The largest value is", max(num2))
    print("Total numbers read is", len(num2))
else:
    print("data2.txt does not exists")
