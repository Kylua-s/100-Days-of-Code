# Exercise 13 - Heads or Tails 
"""
Instructions:
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Example Output:
Heads
or
Tails
"""

# Exercise 13 - Solution
import random

random_int = random.randint(0, 1)

if random_int == 0:
    print("Heads")
else:
    print("Tails")
