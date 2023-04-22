# Exercise 17 - High Score
"""
Instructions:
You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions. 

The output words must match the example. i.e
The highest score in the class is: x

Example Input:
78 65 89 86 55 91 64 89

Example Output:
The highest score in the class is: 91
"""

# Given Code
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Exercise 17 - Solution
heigh_score = 0

for score in student_scores:
  if score > heigh_score:
    heigh_score = score

print(f"The highest score in the class is: {heigh_score}")
