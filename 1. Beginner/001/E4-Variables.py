# Exercise 4 - Variables
"""
Instructions:
Write a program that switches the values stored in the variables a and b.

Example Input:
a: 3
b: 5

Example Output
a: 5
b: 3
"""

# Given Code
a = input("a: ")
b = input("b: ")

# Exercise 4 - Solution
safe = a
a = b
b = safe

# Given Code
print("a: " + a)
print("b: " + b)
