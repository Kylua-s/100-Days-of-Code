# Project 12 - Higher Lower Game
"""
Idea: 
The Higher Lower Game is a simple online quiz game where the objective is to guess which of two presented search terms is more popular in terms of the average monthly search volume on Google. 
The game presents two search terms and the player must choose which term they believe has a higher search volume. 
The player then finds out whether their guess was correct or not, and earns a point for correct answers. 
The game continues with new pairs of search terms until the player is wrong. 
"""

# Project 12 - Solution
import random
import higherLower_art as art
import higherLower_data as data
import os

# initialize variables
score = 0
correct_guess = True
# start the game loop
while correct_guess:
    # clear the console screen and display the game logo
    os.system('cls')
    print(art.logo)

    # display the current score (if it's not the first round)
    if score > 0:
        print(f"You're right! Current score: {score}.")

    # randomly select two accounts to compare
    a_search = random.randint(0, 49)
    b_search = random.randint(0, 49)
    while a_search == b_search:
        b_search = random.randint(0, 49)

    # get the details of the two accounts
    a_name = data[a_search]['name']
    a_follower = data[a_search]['follower_count']
    a_description = data[a_search]['description']
    a_country = data[a_search]['country']

    b_name = data[b_search]['name']
    b_follower = data[b_search]['follower_count']
    b_description = data[b_search]['description']
    b_country = data[b_search]['country']

    # display the details of the two accounts
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
    print(art.vs)
    print(f"Against B: {b_name}, a {b_description}, from {b_country}.")

    # Ask the player to guess and make sure the player's input is valid  
    guess = input("Who has more followers? Type 'A' or 'B': ")
    while guess != 'A' and guess != 'B':
        guess = input("Please type 'A' or 'B': ")

    # check if the player's guess is correct    
    if guess == 'A' and a_follower > b_follower:
        score += 1
    elif guess == 'B' and b_follower > a_follower:
        score += 1
    else: # if the player's guess is incorrect, end the game loop
        print(f"Sorry that's wrong. Final score: {score}.")
        correct_guess = False