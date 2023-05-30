# Project 6 - Hangman
"""
Idea: 
Write a program to play hangman.

Step 1:
Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

Step 2:
Create an empty List called display.
Loop through each position in the chosen_word;
Print 'display' and you should see the guessed letter in the correct position and every other letter replaces with "_".

Step 3:
Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the
chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

Step 4:
Create a variable called 'lives' to keep track of the number of lives left.
If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
If the lives goes down to 0, then the game should stop,
and it should print "You lose."
Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

Step 5:
Update the word list to use the 'word_list' from hangman_words.py
Import the stages from hangman_art.py and make this error go away.
Import the logo from hangman_art.py and print it at the start of the game.
If the user has entered a letter they've already guessed, print the letter and let them know.
If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
"""

# Project 6 - Solution
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}.")

    # Check a guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a live.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])
