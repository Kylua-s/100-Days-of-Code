# Exercise 24 - Days in Month 
"""
Instructions:
In the starting code, you'll find the solution from the Leap Year challenge. 
First, convert this function is_leap() so that instead of printing "Leap year."
Or "Not leap year."
It should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs,
e.g.: days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.: 28
The List month_days contains the number of days in a month from January to December for a non-leap year.
A leap year has 29 days in February.
"""


# Exercise 24 - Solution
def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# Given Code
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
