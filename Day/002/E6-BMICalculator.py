# Exercise 6 - BMI Calculator
"""
Instructions:
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Warning you should convert the result to a whole number.

Example Input:
weight = 80
height = 1.75

Example Output:
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
"""

# Given Code
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Exercise 6 - Solution
height_float = float(height)
weight_float = float(weight)
print(int(weight_float/height_float**2))
