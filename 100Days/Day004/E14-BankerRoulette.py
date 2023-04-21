# Exercise 14 - Banker Roulette
"""
Instructions:
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.

Example Input:
Angela, Ben, Jenny, Michael, Chloe

Example Output:
Michael is going to buy the meal today!
"""

# Given Code
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# Exercise 14 - Solution
import random
random_int = random.randint(0, len(names)-1)
print(f"{names[random_int]} is going to buy the meal today!")