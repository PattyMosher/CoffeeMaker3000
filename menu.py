import self
import coffee_art


class MenuItem:
    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
        """
        Creates MenuItem
        :param name: Name of the item
        :param water: mL of water
        :param milk: ml of milk
        :param coffee: grams of ground coffee
        :param cost: cost of item
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="coffee", water=150, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]

    def get_items(self):
        """
        Returns the name of each menu item
        :return: str: names of menu items as a string
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}, "
        return options

    def get_beverage(self, order_name: str):
        """Returns the menu item with name matching the order_name.
        If no menu item matches the name entered, prints error message
        :param order_name: name of the MenuItem
        :return: MenuItem: item
        """
        for item in self.menu:
            if item.name == order_name:
                return item

