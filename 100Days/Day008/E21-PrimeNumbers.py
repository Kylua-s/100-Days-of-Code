# Exercise 21 - Prime Numbers 
"""
Instructions:
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
You need to write a function that checks whether if the number passed into it is a prime number or not.

Example Input 1:
73
Example Output 1:
It's a prime number.

Example Input 2:
75
Example Output 2:
It's not a prime number.
"""

# Exercise 21 - Solution
def prime_checker(number):
    prime = True

    for x in range(2, number):
        if number % x == 0: 
            prime = False
    
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Given Code
n = int(input("Check this number: "))
prime_checker(number=n)