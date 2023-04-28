# Project 7 - Caesar Cipher
"""
Idea: 
Write a program that allows you to encrypt and decrypt texts using the Caesar cipher, 
a simple substitution cipher that shifts letters a certain number of positions down the alphabet.

Step 1:
TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 
TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

Step 2:
TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable.
You should be able to test the code to encrypt *AND* decrypt a message.

Step 3:
TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

Step 4:
TODO-9: Import and print the logo from art.py when the program starts.
TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
TODO-11: What happens if the user enters a number/symbol/space? Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
"""

# Given Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Project 7 - Solution
import caesar_art

# Function to de- or encrypt a text with the Caesar cipher
def caesar(text, shift, direction):
    cipher_text = ""
    # If the direction is "decode", reverse the shift direction
    if direction == "decode":
        shift *= -1
    # Iterate over each character in the input text
    for char in text:
        # Checking for special characters
        if char in alphabet:
            new_index = alphabet.index(char) + shift
            cipher_text += alphabet[new_index]
        # Otherwise, just append the character
        else:
            cipher_text += char
    print(f"Here's the {direction}d result: {cipher_text}")


print(caesar_art.logo)
code = True
while(code):
    # Get user inputs
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    # For shipt amount greater than 26
    shift_input %= 26
    # Call the Caesar cipher function with the user input
    caesar(text_input, shift_input, direction_input)
    # Ask the user if they want to run the program again
    another_round = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if another_round == "no":
        code = False
        print("Goodbye")
