# Project 13 - Coffee Machine
"""
Coffee Machine Program Requirements:
1. Prompt wish by asking "What would you like?"
2. Turn off the Coffee Machine by entering “off” to the prompt.
3. Print report
4. Check resources sufficient?
5. Process coins
6. Check transaction successful?
7. Make Coffee
"""

# Given Code
# The MENU dictionary has three coffee types and their respective ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# The resource dictionary lists the current amount of ingredients available for making coffee
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Project 13 - Solution
# To keep track of the total sales volume
sales_volume = 0


# Prints the current status of the resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${sales_volume}")


# Checks if there are enough ingredients available to make the selected coffee
def resource_check(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        needed_value = MENU[coffee]['ingredients'][ingredient]
        have_value = resources[ingredient]
        if needed_value > have_value:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


# Prompts the user to input the number of coins to make the payment for the coffee
def coin_insert():
    print("Please insert coins.")
    monetary_value = int(input("How many quarters?: ")) * 0.25
    monetary_value += int(input("How many dimes?: ")) * 0.1
    monetary_value += int(input("How many nickles?: ")) * 0.05
    monetary_value += int(input("How many pennies?: ")) * 0.01
    return monetary_value


# Checks if the user has inserted enough money to pay for the coffee and returns change
def transaction(coffee):
    monetary_value = coin_insert()
    needed_value = MENU[coffee]['cost']
    if monetary_value < needed_value:
        print("“Sorry that's not enough money. Money refunded.")
        return False
    elif monetary_value > needed_value:
        change = round(monetary_value - needed_value, 2)
        print(f"Here is ${change} dollars in change.")
    global sales_volume
    sales_volume += needed_value
    return True


# Reduces the resources available in the resource dictionary
def make_coffee(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
    print(f"Here is your {coffee}. Enjoy!")


on = True
while on:
    # Ask the user for their coffee order, and validate it
    wish = input("What would you like? (espresso/latte/cappuccino): ")
    while wish != 'espresso' and wish != 'latte' and wish != 'cappuccino' and wish != 'report':
        wish = input("Please type 'espresso', 'latte' or 'cappuccino': ")

        # Display the current resources
    if wish == 'report':
        report()
    # Turn the coffee machine off
    elif wish == 'off':
        on = False
    # Otherwise, make the coffee if there are enough resources and the transaction is successful
    else:
        if resource_check(wish):
            if transaction(wish):
                make_coffee(wish)
