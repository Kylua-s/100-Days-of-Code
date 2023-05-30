# Project 23 - NATO Alphabet
"""
Idea:
Create a dictionary from the CSV file named "nato_phonetic_alphabet.csv".
Prompt the user to enter a word.
Iterate over each letter in the word.
Print the letter and its corresponding NATO phonetic code.
"""
import pandas

# Converts the CSV into a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Prints for each letter in the word its corresponding NATO code
word = input("Enter a word: ")
for letter in word:
    if letter != ' ':
        print(f"{letter}: {nato_dict[letter.upper()]}")
