# Project 26 - Flash Cards
"""
Learn the 1000 most commen spanish words.
Words from: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1000
"""
import pandas
import random
import customtkinter as ctk
from PIL import Image

# Reads the csv-file and converts it into a dictionary
words_data = pandas.read_csv("data/spanish_words.csv")
words = words_data.to_dict(orient="records")


# Removes the card from the dict
def right():
    words.remove(current_card)
    next_card()


# Flips the card and shows the translation
def flip_card():
    current = language_text.cget("text")
    if current == "Spanish":
        language_text.configure(text="English")
        word_text.configure(text=current_card["English"])
    else:
        language_text.configure(text="Spanish")
        word_text.configure(text=current_card["Spanish"])


# Shows next card
def next_card():
    global current_card
    current_card = random.choice(words)
    language_text.configure(text="Spanish")
    word_text.configure(text=current_card["Spanish"])


# Window settings
root = ctk.CTk()
root.title("FlashCards")
root.config(padx=50, pady=50)

# Card image
card_image = ctk.CTkImage(dark_image=Image.open("images/Card.png"), size=(778, 501))
card_label = ctk.CTkLabel(root, image=card_image, text="").grid(column=1, row=1, columnspan=3, rowspan=2)

# Card Text
language_text = ctk.CTkLabel(card_label, font=("Arial", 40, "italic"), text_color="#f7f4f3", fg_color="#737373")
language_text.grid(column=1, row=1, columnspan=3)

word_text = ctk.CTkLabel(card_label, font=("Arial", 60, "bold"), text_color="#f7f4f3", fg_color="#737373")
word_text.grid(column=1, row=1, columnspan=3, rowspan=3)

# For the Space between
space_label = ctk.CTkLabel(root, text="", pady=10).grid(column=1, row=3, columnspan=3)

# Buttons
check_image = ctk.CTkImage(dark_image=Image.open("images/Check.png"), size=(95, 95))
check_button = ctk.CTkButton(root, image=check_image, fg_color="transparent", hover_color="#404040", width=0, text="",
                             command=next_card).grid(column=1, row=4)

switch_image = ctk.CTkImage(dark_image=Image.open("images/Flip.png"), size=(95, 95))
switch_button = ctk.CTkButton(root, image=switch_image, fg_color="transparent", hover_color="#404040", width=0, text="",
                              command=flip_card).grid(column=2, row=4)

cross_image = ctk.CTkImage(dark_image=Image.open("images/Cross.png"), size=(95, 95))
cross_button = ctk.CTkButton(root, image=cross_image, fg_color="transparent", hover_color="#404040", width=0, text="",
                             command=next_card).grid(column=3, row=4)

current_card = {}
next_card()
root.mainloop()
