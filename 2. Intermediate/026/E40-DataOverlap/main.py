# Exercise 40 - Data Overlap
"""
Instructions:
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result, which contains the numbers that are common in both files.
IMPORTANT: The result should be a list that contains Integers, not Strings.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
"""

# Exercise 40 - Solution
# Gets all data from both files
with open("file1.txt") as file1:
    f1_numbers = [num.rstrip() for num in file1]

with open("file2.txt") as file2:
    f2_numbers = [num.rstrip() for num in file2]

# Creates a list, which contains the numbers that are common in both files.
result = [int(num) for num in f1_numbers if num in f2_numbers]
print(result)
