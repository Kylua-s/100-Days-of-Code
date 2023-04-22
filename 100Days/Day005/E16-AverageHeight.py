# Exercise 16 - Average Height
"""
Instructions:
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. 
You should try to replicate their functionality using what you have learnt about for loops.

Example Input:
156 178 165 171 187

Example Output:
171
"""

# Given Code
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Exercise 16 - Solution
height_total = 0
students_total = 0

# Adding all heights together and counting the students
for student in student_heights:
  height_total += student
  students_total += 1

# Calculating the average hight and rounding it
avg_height = round(height_total / students_total)
print(avg_height)