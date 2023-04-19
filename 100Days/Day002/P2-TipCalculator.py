# Project: Tip Calculator
"""
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""
print("Welcome to the tip calculator.")

# Asking the user for inputs and converting them
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating the bill plus tip per person
bill_and_tip = (bill / people) * (tip_percentage / 100 + 1)

# Formatting the result
bill_and_tip = round(bill_and_tip, 2)
bill_and_tip = "{:.2f}".format(bill_and_tip)

print(f"Each person should pay: ${bill_and_tip}")
