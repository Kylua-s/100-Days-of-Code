# Exercise 43 - Args
"""
Introcution:
Create a function to make an unlimited number of arguments.
"""


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(1, 2, 3, 4, 5))
