# Exercise 7 - Life in Weeks 
"""
Instructions:
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
1 year = 365 days, 52 week or 12 months
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.

Example Input:
56

Example Output:
You have 12410 days, 1768 weeks, and 408 months left.
"""

# Given Code
age = input("What is your current age? ")

# Exercise 7 - Solution
time_left = 90 - int(age)
print(f"You have {time_left*365} days, {time_left*52} weeks, and {time_left*12} months left.")