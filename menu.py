import self
import coffee_art

class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
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
    def get_items(self): # returns names of menu items as a string
        items =""
        return items


    def find_beverage(self, order_name): # returns MenuItem with order_name, or None
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"Error 418: I am not a teapot.")
        print(coffee_art.teapot)