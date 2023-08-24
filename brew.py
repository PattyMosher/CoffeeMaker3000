import time
from menu import *
import coffee_art


class CoffeeBrewer:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        """Prints the amounts of water, milk, and coffee in the machine"""
        print(f"Water:   {self.resources['water']}mL")
        print(f"Milk:    {self.resources['milk']}mL")
        print(f"Coffee:  {self.resources['coffee']}g")

    def is_sufficient_resources(self, beverage: MenuItem):
        """Checks if enough of each ingredient required for the item required.
        :param beverage: MenuItem
        :return: bool: True if enough of all ingredients for item
        """
        for ingredient in beverage.ingredients:
            if self.resources[ingredient] < beverage.ingredients[ingredient]:
                print(f" Sorry. Not enough {ingredient} to make a {beverage.name}.")
                return False
            else:
                return True

    def brew(self, beverage: MenuItem):
        """Brews the beverage
        :param beverage: MenuItem that was ordered
        """
        for ingredient in beverage.ingredients:
            self.resources[ingredient] -= beverage.ingredients[ingredient]
            print("Brewing...")
            time.sleep(1)
        if beverage.name == "coffee":
            print(coffee_art.coffee)
        elif beverage.name == "latte":
            print(coffee_art.latte)
        else:
            print(coffee_art.cappuccino)
        print("Share and Enjoy!")


    def resupply(self):
        """Increases each resource by amount user enters for each"""
        print(self.report())
        for item in self.resources:
            self.resources[item] += int(input(f"How much {item} would you like to add:  "))
