# Exercise 1 - Printing
"""
Instructions:
Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

Example Output:
After you have written your code, you should run your program and it should print the following:
Day 1 - Python Print Function
The function is declared like this:
print('what to print')
"""

# Exercise 1 - Solution
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")


# Exercise 2 - Debugging Practice
"""
Instructions:
Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.

Example Output:
When you run your program, it should print the following:
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.

Fix the code below 👇
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
"""

# Exercise 2 - Solution
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Exercise 3 - Input Function
"""
Instructions:
Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

Example Input:
Angela

Example Output:
6
"""

# Exercise 3 - Solution
print(len(input('What is your name? ')))


# Exercise 4 - Variables
"""
Instructions:
Write a program that switches the values stored in the variables a and b.

Example Input:
a: 3
b: 5

Example Output
a: 5
b: 3

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇




#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
"""

# Exercise 4 - Solution
a = input("a: ")
b = input("b: ")

safe = a
a = b
b = safe

print("a: " + a)
print("b: " + b)
