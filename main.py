# CoffeeMaker3000
import time

from brew import CoffeeBrewer
from menu import Menu, MenuItem
from money import Money
import coffee_art

brewer = CoffeeBrewer()
menu = Menu()
funds = Money()
on = True

while on:
    print(coffee_art.coffee_machine)
    options = menu.get_items()
    order = input("What would you like to order? I can make:\n" + options).lower()
    if order == "resupply":
        brewer.resupply()
    elif order == "report":
        brewer.report()
        funds.report()
    elif order == "off":
        print("Shutting down")
        on = False
    elif order not in menu.get_items():
        # Because it's not a proper coffee maker simulation without a 418.
        print(f"Error 418: I am not a teapot.\n{coffee_art.teapot}\nI can only make {menu.get_items()}.")

    else:
        beverage = menu.get_beverage(order)
        if brewer.is_sufficient_resources(beverage):
            if funds.process_payment(beverage.cost):
                brewer.brew(beverage)
    time.sleep(3)


