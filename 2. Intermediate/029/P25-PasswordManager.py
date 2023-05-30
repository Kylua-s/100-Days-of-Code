# Project 25 - Password Manager

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


# Generates a random password with letters, digites, and symols
def generate_password():
    password_list = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12)]
    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Checks the entries and saves everything into the data.txt file
def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {mail} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {mail} | {password}\n")
                website_entry.delete(0, tk.END)
                mail_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# Window settings
root = tk.Tk()
root.title("Open Lock")
root.config(padx=20, pady=20)


# Image
canvas = tk.Canvas(width=200, height=224, highlightthickness=0)
image = tk.PhotoImage(file="Logo.png")
canvas.create_image(100, 112, image=image)
canvas.grid(column=1, row=1, columnspan=3)


# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=1, row=2, sticky="e")

mail_label = tk.Label(text="Email/Username:")
mail_label.grid(column=1, row=3, sticky="e")

password_label = tk.Label(text="Password:")
password_label.grid(column=1, row=4, sticky="e")


# Enteries
website_entry = tk.Entry(width=44)
website_entry.grid(column=2, row=2, columnspan=2, sticky="w")
website_entry.focus()

mail_entry = tk.Entry(width=44)
mail_entry.grid(column=2, row=3, columnspan=2, sticky="w")

password_entry = tk.Entry(width=25)
password_entry.grid(column=2, row=4, sticky="w")


# Buttons
generate_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=3, row=4, sticky="w")

add_button = tk.Button(text="Add", width=37, command=save)
add_button.grid(column=2, row=5, columnspan=2, sticky="w")


root.mainloop()
