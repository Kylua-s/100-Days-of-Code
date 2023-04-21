# Project 4 - Rock Paper Scissors
"""
Idea:
Write a rock, paper, scissors program in which the user plays against the computer.
"""

# Given Code
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Project 4 - Solution
import random

computer = random.randint(0, 2)
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
weapons = [rock, paper, scissors]

print("The computer chooses:")
print(weapons[computer])
print("You choose:")
print(weapons[player])

if computer == player: 
  print("It's a draw") 
elif computer == 0 and player == 1:
  print("You win!")
elif computer == 0 and player == 2:
  print("You lose")
elif computer == 1 and player == 0:
  print("You lose")
elif computer == 1 and player == 2:
  print("You win!")
elif computer == 2 and player == 0:
  print("You win!")
elif computer == 2 and player == 1:
  print("You lose")