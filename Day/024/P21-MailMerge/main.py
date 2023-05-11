# Project 21 - Mail Merge
# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name
# Save the letters in the folder "ReadyToSend"

# Project 21 - Solution
# Opens the default letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

# Opens the file with name
with open("./Input/Names/invited_names.txt") as name_file:
    for name in name_file:
        name = name.rstrip()
        named_letter = letter.replace('[name]', name)
        # Creates a new file with the right adressed letter
        with open(f"./Output/ReadyToSend/{name}_letter.txt", 'x') as final_letter:
            final_letter.write(named_letter)
