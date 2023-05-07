# Exercise 17 - High Score
"""
Instructions:
You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions. 

The output words must match the example.
The highest score in the class is: x

Example Input:
78 65 89 86 55 91 64 89

Example Output:
The highest score in the class is: 91
"""

# Given Code
student_scores = input("Input a list of student scores: ").split()

# Exercise 17 - Solution
high_score = 0

# # Converts the scores into integers
student_scores = [int(score) for score in student_scores]

for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")
