# Project 9 - Calculator
"""
Idea:
Build a calculator.
"""

# Project 9 - Solution
import calculator_art
import os

def calculation(number1, operator, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        return number1 / number2

# While the user wants to calculate
while True:
    print(calculator_art.logo)
    number1 = int(input("What's your first number?: "))

    # While the user want to calculate with the same result
    while True:
        print("+\n-\n*\n/")

        operator = input("Pick an operator: ")
        number2 = int(input("What's the next number?: "))
        result = calculation(number1, operator, number2)

        print(f"{number1} {operator} {number2} = {result}")

        go_on = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'exit' if you're finished: ")

        # If the user doesn't want to continue
        if go_on == 'n' or go_on == 'exit':
            os.system('cls')
            break
        number1 = result
        print(f"Your first number is: {result}")

    # If the user wants to end the program
    if go_on == 'exit':
        break