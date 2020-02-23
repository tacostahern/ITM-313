'''
This program will ask the user to enter integer numbers and will stop when the user enters
-99999. When the program ends, it will print out the sum of all the numbers entered, the average,
smallest and largest number entered.
Author: Tony Acosta Hernandez
Course: ITM 313
'''

sum = 0
average = 0
largest = -99999
total_num = 0

num = int(input("Please enter any integer number, or enter -99999 to stop: "))
smallest = num
while (num != -99999):
    sum += num
    if (largest < num):
        largest = num
    if (smallest > num):
        smallest = num
    total_num += 1
    num = int(input("Please enter any integer number, or enter -99999 to stop: "))

print("The sum of all numbers entered is", sum)
print("The average of all the numbers entered is", (sum/total_num))
print("The smallest number entered is", smallest)
print("The largest number entered is", largest)
    
    
