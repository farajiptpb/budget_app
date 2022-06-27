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
        return amount

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

    def __str__(self):

        stars_nums = 30 - len(self.name)
        left_stars_nums = (stars_nums // 2)
        right_stars_nums = (stars_nums - left_stars_nums)
        left_stars = left_stars_nums * '*'
        right_stars = right_stars_nums * '*'

        text = f'{left_stars}Food{right_stars}'
        index = 0
        for dic in self.ledger:
            amount = self.ledger[index]['amount']
            amount = float(amount)
            amount = str(amount)
            if len(amount.split('.')[1]) < 2:
                amount = amount + '0'
            else:
                amount = round(float(amount), 2)
                amount = str(amount)
            des = self.ledger[index]['description']
            len_amount = len(amount[0:7])
            len_descr = len(des[0:23])
            len_white_space = (30 - len_descr - len_amount) * ' '

            text = text + f"\n{des[0:23]}{len_white_space}{amount[0:7]}"
            index = index + 1
        text = text + f"\nTotal: {self.get_balance()}"
        return text


food = Category('food')
food.deposit(1000, 'rice and meat')
food.withdraw(200, 'car')
food.withdraw(200, 'bar')
print(food)
