# Exercise 5 - Data Types
"""
Instructions:
Write a program that adds the digits in a 2-digit number.
E.g., if the input was 35, then the output should be 3 + 5 = 8

Example Input:
39

Example Output:
3 + 9 = 12
12
"""

# Given Code
two_digit_number = input("Type a two digit number: ")

# Exercise 5 - Solution
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
print(num1 + num2)
