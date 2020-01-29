'''
Homework due 1/30/2020
This program will accept an input book code, the book's single copy cost,
the current number of volumes on hand, the prospective class enrollment,
and data that indicates whether the book is required or recommended. and
has or has not been used in the past. Each book is identified by one-letter
subject code followed by an integer book code. The output should show all
input information together with the number of books that must be ordered
(if any), the total cost of all books ordered, and the expected profit if
the store pays 80% of the list price.
Author: Tony Acosta Hernandez
Course: ITM 313
'''
print("Hello user!")
book_code = input("Please enter the book code: ")
book_cost = eval(input("Please enter the book's single copy cost: "))
num_volumes = int(input("Please enter the current number of volumes: "))
class_enrollment = int(input("Please enter the prospective class enrollment: "))
req_rec = input("Is this book required or recommended? ")
us_un = input("Has the book been used or unused? ")

if class_enrollment > num_volumes:
    must_order = class_enrollment - num_volumes
    total_cost = must_order * book_cost
else:
    must_order = 0
    total_cost = 0
expected_profit = total_cost * 0.2

print("So, from the information entered: ")
print("The book code is", book_code)
print("The cost of the book is $%.2f" % (book_cost))
print("The number of volumes is", num_volumes)
print("Class enrollment is", class_enrollment, "students")
print("The book is", req_rec, "and it is", us_un)
print("The amount of books that must be ordered is", must_order)
print("The total cost of the books is $%.2f" % (total_cost))
print("The expected profit is $%.2f" % (expected_profit))
