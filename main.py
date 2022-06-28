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


def create_spend_chart():
    pass


food = Category('food')
entertainment = Category('entertainment')
food.deposit(1000, 'rice and meat')
food.withdraw(200, 'car')
food.withdraw(200, 'bar')
food.transfer(100, entertainment)
print(food)


"""
layer = ('o  ', '   ', '')
lis = ['food', ]

a = 4 - len(lis)
for i in range(a):
    lis.append('')

print(lis)

os_1 = []

if lis[0] != '':
    for index in range(4):
        os_1.append('   ')
    for index in range(7):
        os_1.append('o  ')
else:
    for index in range(11):
        os_1.append('')

os_2 = []

if lis[1] != '':
    for index in range(4):
        os_2.append('   ')
    for index in range(7):
        os_2.append('o  ')
else:
    for index in range(11):
        os_2.append('')

os_3 = []

if lis[2] != '':
    for index in range(4):
        os_3.append('   ')
    for index in range(7):
        os_3.append('o  ')
else:
    for index in range(11):
        os_3.append('')

os_4 = []
if lis[3] != '':
    for index in range(4):
        os_4.append('   ')
    for index in range(7):
        os_4.append('o  ')
else:
    for index in range(11):
        os_4.append('')


percentages = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']

index = 0
t = f""
for i in percentages:
    t = t + f"{i} {os_1[index]}{os_2[index]}{os_3[index]}{os_4[index]}\n"
    index = index + 1

print(t)


def first_str_part():
    pass



"""