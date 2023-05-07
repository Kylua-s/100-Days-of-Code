# Project 10 - Blackjack
"""
Idea:
Write a program to play blackjack.

Our Blackjack House Rules: 
The deck is unlimited in size. 
There are no jokers. 
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""

import blackjack_art
import random
import os


# Given Code
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Project 10 - Solution
# Initialize the game loop
feeling_lucky = True
while feeling_lucky:
    print(blackjack_art.logo)

    # Initialize/ reset the player's and computer's hand
    player_hand = []
    computer_hand = []

    # Deal, calculate and print the player's hand
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_score = sum(player_hand)
    print(f"Your cars: {player_hand}, current score: {player_score}")

    # Deal, calculate and print only the computer's first card
    computer_hand.append(random.choice(cards))
    print(f"Computer's first card: {computer_hand[0]}")
    computer_hand.append(random.choice(cards))
    computer_score = sum(computer_hand)

    # Allow the player to hit until they choose to pass or bust
    while player_score <= 21:
        go_on = input("Type 'y' to get another card, type 'n' to pass: ")
        if go_on == 'y':
            player_hand.append(random.choice(cards))
            player_score = sum(player_hand)
        else:
            break
        # Check for aces
        if 11 in player_hand and player_score > 21:
            ace = player_hand.index(11)
            player_hand[ace] = 1
        print(f"Your cars: {player_hand}, current score: {player_score}")

    # Print the player's final hand and score
    print(f"Your final hand: {player_hand}, final score: {player_score}")

    # Allow the computer to hit until they reach a score of 17 or higher
    if player_score <= 21:
        while computer_score < 17:
            computer_hand.append(random.choice(cards))
            computer_score = sum(computer_hand)
            # Check for aces
            if 11 in computer_hand and computer_score > 21:
                ace = computer_hand.index(11)
                computer_hand[ace] = 1

    # Print the computer's final hand and score
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    # Determine the winner of the game
    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("The computer went over. You win")
    elif player_score > computer_score:
        print("You win")
    elif player_score < computer_score:
        print("You lose")
    elif player_score == computer_score:
        print("Draw")

    # Ask the player if they want to play again
    feeling_lucky = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if feeling_lucky == 'y':
        feeling_lucky = True
        # Clear the console screen
        os.system('cls')
    else:
        feeling_lucky = False
