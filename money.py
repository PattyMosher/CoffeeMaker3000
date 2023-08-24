class Money:
    CURRENCY = "$"
    COIN_VALUES = {
        "loonies": 1.00,
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles":0.05
    }

    def __init__(self):
        self.money = 0
        self.money_received = 0

    def report(self):
        """Prints the total amount of money in the machine"""
        print(f"Total:  {self.CURRENCY}{self.money}")

    def accept_coins(self):
        """Prompts user to insert coins and adds total value fo the coins"""
        print("Please insert coins:")
        for coins in self.COIN_VALUES:
            value = float(input(f"How many {coins}?:  ")) * self.COIN_VALUES[coins]
            self.money_received += float(value)
        return self.money_received

    def process_payment(self, cost: float):
        """Adds the cost to the machine's money if money received is sufficient.
        :param cost: cost of the MenuItem ordered
        :return: bool: True if money received >= cost
        """
        self.accept_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Your change:  {self.CURRENCY}{change}")
            self.money += cost
            self.money_received = 0
            return True
        else:
            change = round(self.money_received, 2)
            print(f"Insufficient funds. Returning {change}")
            self.money_received = 0
            return False

