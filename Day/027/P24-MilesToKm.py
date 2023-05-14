# Project 24 - Mile to Km
"""
Idea:
Create a GUI, which converts miles into kilometers.
"""

import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")


def calculate(miles):
    km = miles * 1.60934
    km_total.config(text=km)


# Labels
miles_lable = tk.Label(text="Miles")
miles_lable.grid(column=3, row=1)

is_lable = tk.Label(text="is equal to")
is_lable.grid(column=1, row=2)

km_total = tk.Label(text="0")
km_total.grid(column=2, row=2)

km_lable = tk.Label(text="Km")
km_lable.grid(column=3, row=2)

# Entry
entry = tk.Entry(width=10)
entry.grid(column=2, row=1)

# Button
button = tk.Button(text="Calculate", command=lambda: calculate(int(entry.get())))
button.grid(column=2, row=3)

window.mainloop()
