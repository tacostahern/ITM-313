import random
'''
This program will generate two positive one digit integers for a user, who will
then be asked to enter what the product of those number is. Should they get the
right answer, they will be congratulated and offered a chance to continue doing
problems. If they get it wrong, the program will ask them to try again and repeat
the same question.
Author: Tony Acosta Hernandez
Course: ITM 313
'''
answer = 'y'

while (answer.lower() == 'y'):
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    product = number1 * number2
    print(number1, "*", number2)
    p_input = int(input("What is the product? "))
    while (p_input != product):
        p_input = int(input("Please try again. "))
    print("That's correct! Good Job!")
    answer = input("Do you want another? <y/n>?")
print("Thank you!")
