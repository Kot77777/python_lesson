class MoneyBox:

    def __init__(self, value=0, number=0):
        self.value = value
        self.number = number

    def add_coin(self, value):
        self.value += value
        self.number += 1

    def get_coins_number(self):
        return self.number

    def get_coins_value(self):
        return self.value