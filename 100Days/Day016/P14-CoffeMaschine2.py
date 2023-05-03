# Project 14 - Coffe Maschine 2
"""
Coffee Machine Program Requirements:
1. Prompt wish by asking “What would you like?
2. Turn off the Coffee Machine by entering “off” to the prompt.
3. Print report
4. Check resources sufficient?
5. Process coins
6. Check transaction successful?
7. Make Coffee

Important:
Use the methods from the other classes!
"""

# Project 14 - Solution
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    # Ask the user for their coffee order
    wish = input(f"What would you like? ({menu.get_items()}): ")

    # Display the current resources
    if wish == 'report':
        coffee_maker.report()
        money_machine.report()

    # Turn the coffee machine off
    elif wish == 'off':
        on = False

    # Otherwise, make the coffee if there are enough resources and the transaction is successful
    else:
        coffee = menu.find_drink(wish)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)