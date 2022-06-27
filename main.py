class Category:
    def __init__(self, name, ledger=None):
        if ledger is None:
            ledger = []
        self.name = name
        self.ledger = ledger

    def deposit(self, amount, description=''):
        dictionary = dict()
        dictionary['amount'] = amount
        dictionary['description'] = description
        self.ledger.append(dictionary)

    def withdraw(self, amount, description=''):
        dictionary = dict()
        dictionary['amount'] = -amount
        dictionary['description'] = description
        funds = 0
        for dic in self.ledger:
            funds = funds + dic['amount']
        if self.check_funds(amount=amount):
            self.ledger.append(dictionary)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for dic in self.ledger:
            balance = balance + dic['amount']
        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount=amount):
            self.withdraw(amount=amount, description=f"Transfer to {destination.name}")
            destination.deposit(amount=amount, description=f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False


food = Category('food')
clothing = Category('clothing')
food.deposit(300, 'for meat')
food.deposit(400, 'for rice')
food.withdraw(40000, 'buy some rice and meat')
food.transfer(200, clothing)
print(food.withdraw(50))
print(food.get_balance())
print(clothing.check_funds(300))
print(clothing.ledger)
print(food.ledger)
