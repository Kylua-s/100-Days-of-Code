# Project 29- Quizzler
"""
A quiz with random true/ false questions.
"""
import customtkinter as ctk
from PIL import Image
import requests
import html

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()
question_data = data["results"]
position = 0
score = 0


# Shows the next question
def next_question():
    question.configure(state="normal")
    question.delete("0.0", "end")
    if position < 2:
        question.insert("0.0", html.unescape(data["results"][position]["question"]))
        question.configure(state="disabled")
    else:
        question.insert("0.0", f"Your Score is {score} out of 10!")
        question.configure(state="disabled")
        root.after(3000)
        root.destroy()


# If the user clicks the correct button
def right():
    if question_data[position]["correct_answer"] == "True":
        guess = True
    else:
        guess = False
    feedback(guess)


# If the user clicks the wrong button
def wrong():
    if question_data[position]["correct_answer"] == "False":
        guess = True
    else:
        guess = False
    feedback(guess)


# Show the user if there answer is right
def feedback(guess):
    if guess:
        question.configure(state="normal", fg_color="#2cba00")
        global score
        score += 1
        score_label.configure(text=f"Score: {score}")
    else:
        question.configure(state="normal", fg_color="#ff0000")

    root.after(1000)
    question.configure(state="disabled", fg_color="#1D1E1E")
    global position
    position += 1
    next_question()


# Window settings
root = ctk.CTk()
root.title("Quizzler")
root.config(padx=50, pady=50)

# Labels
score_label = ctk.CTkLabel(root, text="Score: 0", font=("Arial", 15, "bold"))
score_label.grid(column=2, row=1)

# Card Text
question = ctk.CTkTextbox(root, width=400, height=250, wrap="word", font=("Arial", 22, "italic"))
question.grid(column=1, row=2, columnspan=2)

# For the Space between
space = ctk.CTkLabel(root, text="", pady=10).grid(column=1, row=3, columnspan=2)

# Buttons
check_image = ctk.CTkImage(dark_image=Image.open("../../2. Intermediate/031/images/Check.png"), size=(95, 95))
check_button = ctk.CTkButton(root, image=check_image, fg_color="transparent", hover_color="#404040", width=0, text="",
                             command=right).grid(column=1, row=4)

cross_image = ctk.CTkImage(dark_image=Image.open("../../2. Intermediate/031/images/Cross.png"), size=(95, 95))
cross_button = ctk.CTkButton(root, image=cross_image, fg_color="transparent", hover_color="#404040", width=0, text="",
                             command=wrong).grid(column=2, row=4)

next_question()
root.mainloop()
