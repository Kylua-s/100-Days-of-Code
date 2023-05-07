# Exercise 22 - Grading Program
"""
Instructions:
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores
are the names of the students and the values are their exam scores. Write a program that converts their 
scores to grades. By the end of your program, you should have a new dictionary called student_grades 
that should contain student names for keys and their grades for values. The final version of the 
student_grades dictionary will be checked. 

This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

Expected Output:
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable',
'Neville': 'Fail'}'
"""

# Given Code
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Exercise 22 - Solution
student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score <= 70:
        student_grades[key] = "Fail"
    elif score <= 80:
        student_grades[key] = "Acceptable"
    elif score <= 90:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Outstanding"

print(student_grades)
