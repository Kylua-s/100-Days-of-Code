# Project 11 - Guess The Number
# The name says it all
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Please type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 10

guess = 0
while guess != number and attempts > 0:
    print(f"You have {attempts} left to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        print("Guess again.")
    elif guess < number:
        print("Too low.")
        print("Guess again.")
    attempts -= 1

if guess == number:
    print(f"You got it! The number is {number}.")
else:
    print("You went out of attempts.")
    print(f"The number was {number}.")