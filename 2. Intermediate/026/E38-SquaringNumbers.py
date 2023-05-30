# Exercise 38 - Squaring Numbers
"""
Instructions:
You are going to write a List Comprehension to create a new list called squared numbers.
This new list should contain every number in the list numbers but each number should be squared.

Example Output
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
"""

# Given Code
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Exercise 38 - Solution
squared_numbers = [num*num for num in numbers]
print(squared_numbers)
