'''
This program will ask the user to enter 2 grades for 2 courses as well as the
number of credit hours each course is worth. It will then calculate the GPA of
the user based on this information and then display it. The program will also
offer the user a warning message if their GPA is less than 2.0 or a
congratulatory message if their GPA is 3.5 or above.
Author: Tony Acosta Hernandez
Course: ITM 313
'''

first_grade = input("Please enter your letter grade for the first course: ")

if (first_grade.lower() == "a"):
    fgrade_points = 4.0
elif (first_grade.lower() == "b"):
    fgrade_points = 3.0
elif (first_grade.lower() == "c"):
    fgrade_points = 2.0
elif (first_grade.lower() == "d"):
    fgrade_points = 1.0
elif (first_grade.lower() == "f"):
    fgrade_points = 0.0
else:
    print("Not a valid grade, so you get an F")
    fgrade_points = 0.0
    
first_ch = int(input("Please enter the number of credits it is worth: "))

second_grade = input("Please enter your letter grade for the second course: ")

if (second_grade.lower() == "a"):
    sgrade_points = 4.0
elif (second_grade.lower() == "b"):
    sgrade_points = 3.0
elif (second_grade.lower() == "c"):
    sgrade_points = 2.0
elif (second_grade.lower() == "d"):
    sgrade_points = 1.0
elif (second_grade.lower() == "f"):
    sgrade_points = 0.0
else:
    print("Not a valid grade, so you get an F")
    sgrade_points = 0.0
    
second_ch = int(input("Please enter the number of credits it is worth: "))

total_gp = (fgrade_points * first_ch) + (sgrade_points * second_ch)
gpa = total_gp/(first_ch + second_ch)

if (fgrade_points < sgrade_points):
    print("Here are the grades you entered:", first_grade.capitalize(), "and", second_grade.capitalize())
    print("Here are the credit hours you entered:", first_ch, "and", second_ch)
    print("Your calculated GPA: %.2f" % (gpa))
else:
    print("Here are the grades you entered:", second_grade.capitalize(), "and", first_grade.capitalize())
    print("Here are the credit hours you entered:", second_ch, "and", first_ch)
    print("Your calculated GPA: %.2f" % (gpa))

if (gpa < 2.0):
    print("Please try harder")
elif (gpa >= 3.5):
    print("You are trying hard!")


