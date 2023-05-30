# Exercise 44 - IndexError Handling
"""
Instructions:
We've got some buggy code. Try running the code. The code will crash and give you an IndexError.
This is because we're looking through the list of fruits for an index that's out of range.
If the user enters something that's out of range, just print a default output of “Fruit pie”.
"""

# Given Code
fruits = ["Apple", "Pear", "Orange"]


# Exercise 44 - Solution
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# Given Code
make_pie(4)
