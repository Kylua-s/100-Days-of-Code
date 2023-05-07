# Exercise 12 - Love Calculator
"""
Instructions:
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:
Take both people's names and check for the number of times, the letters in the word TRUE occur.
Then check for the number of times the letters in the word LOVE occur.
Then combine these numbers to make a 2-digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

Example Input 1:
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1:
Your score is 42, you are alright together.

Example Input 2:
name1 = "Brad Pitt"
name2 = "Jennifer Anniston"
Example Output 2
Your score is 73.
"""

# Given Code
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Exercise 12 - Solution
names = name1 + name2
names = names.lower()

# Counting for the letters t, r, u, e
true_count = names.count('t')
true_count += names.count('r')
true_count += names.count('u')
true_count += names.count('e')

# Counting the letters l, o, v, e
love_count = names.count('l')
love_count += names.count('o')
love_count += names.count('v')
love_count += names.count('e')

# Checking the compatibility
compatibility = (str(true_count) + str(love_count))
compatibility = int(compatibility)

if compatibility < 10 or compatibility > 90:
    print(f"Your score is {compatibility}, you go together like coke and mentos.")
elif 40 < compatibility < 50:
    print(f"Your score is {compatibility}, you are alright together.")
else:
    print(f"Your score is {compatibility}.")
