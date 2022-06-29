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


def create_spend_chart(categories):
    category_os = list()

    withdraw = 0
    total_withdraw = 0
    for category in categories:
        for dic in category.ledger:
            if dic['amount'] < 0:
                total_withdraw = total_withdraw + dic['amount']
    for category in categories:
        for dic in category.ledger:
            if dic['amount'] < 0:
                withdraw = withdraw + dic['amount']
        category_os.append(abs(int(10 * round((withdraw/total_withdraw), 2))))
        withdraw = 0
        deposit = 0
    len_ctg = len(categories)
    a = 4 - len_ctg
    for i in range(a):
        categories.append('')

    os_1 = []
    if categories[0] != '':
        o_range = category_os[0]
        for index in range(10 - o_range):
            os_1.append('   ')
        for index in range(o_range):
            os_1.append('o  ')
    else:
        for index in range(10):
            os_1.append('')

    os_2 = []
    if categories[1] != '':
        o_range = category_os[1]
        for index in range(10 - o_range):
            os_2.append('   ')
        for index in range(o_range):
            os_2.append('o  ')
    else:
        for index in range(10):
            os_2.append('')

    os_3 = []
    if categories[2] != '':
        o_range = category_os[2]
        for index in range(10 - o_range):
            os_3.append('   ')
        for index in range(o_range):
            os_3.append('o  ')
    else:
        for index in range(10):
            os_3.append('')

    os_4 = []
    if categories[3] != '':
        o_range = category_os[3]
        for index in range(10 - o_range):
            os_4.append('   ')
        for index in range(o_range):
            os_4.append('o  ')
    else:
        for index in range(10):
            os_4.append('')

    percentages = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|']
    index = 0
    t = f"Percentage spent by category\n"
    for i in percentages:
        t = t + f"{i} {os_1[index]}{os_2[index]}{os_3[index]}{os_4[index]}\n"
        index = index + 1

    t = t + "  0| "

    for i in range(len_ctg):
        t = t + "o  "

    dashes = (3 * len_ctg + 1)*'-'
    t = t + '\n    ' + dashes

    categories_name = []

    for ctg in categories:
        if ctg != '':
            categories_name.append(ctg.name)

    for i in range(a):
        categories_name.append('')
    len_name = {}
    for name in categories_name:
        len_name[f"{name}"] = len(name)

    name_spells = {}
    for name in categories_name:
        spell = []
        for letter in name:
            spell.append(letter)
        name_spells[f"{name}"] = spell

    max_name_range = max(len_name.values())

    for name in name_spells.values():

        if name:
            for i in range(max_name_range - len(name)):
                name.append('  ')
        else:
            for i in range(max_name_range - len(name)):
                name.append('')

    for name in name_spells.values():

        for l in name:
            if l == '  ':
                name[name.index(l)] = f"{l} "
            elif l == '':
                name[name.index(l)] = f"{l}"
            else:
                name[name.index(l)] = f"{l}  "
    first = name_spells[categories_name[0]]
    first[0] = first[0].title()
    second = name_spells[categories_name[1]]
    second[0] = second[0].title()
    third = name_spells[categories_name[2]]
    third[0] = third[0].title()
    fourth = name_spells[categories_name[3]]
    fourth[0] = fourth[0].title()

    t = t + f"\n"
    for i in range(max_name_range):
        if i < max_name_range - 1:
            br = '\n'
        else:
            br = ''

        t = t + f"     {first[i]}{second[i]}{third[i]}{fourth[i]}{br}"

    print(t)
food = Category('food')
entertainment = Category('entertainment')
business = Category('business')

food.deposit(900, 'rice and meat')
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

categories = []
categories.append(business)
categories.append(food)
#categories.append(entertainment)

create_spend_chart(categories)
