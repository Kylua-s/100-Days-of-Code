# Exercise 20 - Paint Area Calculator
"""
Instructions:
You are painting a wall.
The instructions on the paint can say that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

Example Input:
test_h = 3
test_w = 9

Example Output:
You'll need 6 cans of paint.
"""

# Exercise 20 - Solution
import math


def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans = math.ceil(cans)
    print(f"You'll need {cans} cans of paint.")


# Given Code
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
