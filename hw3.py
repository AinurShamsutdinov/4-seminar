# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

COM = 1.5
COM_LIMIT = 600
RICH_TAX = 10
POOR_LEVEL = 5_000_000
QUIT = 'quit'
ADD = 'add'
WITHDRAW = 'draw'
EXIT_COMMAND = 'quit'
INTEREST_RATE = 3
INTEREST_TIME = 3


def add_to_account():
    global account
    global count_operation
    global operations
    add_money = float(input('Enter amount to add: '))
    commis = add_money * COM / 100
    amount = (add_money - commis)
    account += amount
    count_operation += 1
    operations.append(add_money)
    return amount


def withdraw_from_account():
    global account
    global count_operation
    global operations
    draw = float(input('Enter amount to withdraw: '))
    commis_with = draw * COM / 100
    amount_draw = (draw + commis_with)
    if amount_draw < account:
        account -= amount_draw
        print(f'Amount withdrawn with commission {amount_draw}')
    else:
        print(f'Not enough founds to withdraw with tax and commission: {amount_draw}')
    count_operation += 1
    operations.append(-draw)
    return draw


def calc_interest():
    global account
    global count_operation
    interest_calc = account * INTEREST_RATE / 100
    account += interest_calc
    count_operation = 0
    return interest_calc


def tax_pay():
    global account
    tax_to_pay = account * RICH_TAX / 100
    account -= tax_to_pay
    return tax_to_pay


def start_operations():
    while account != EXIT_COMMAND:
        action = input('Enter action: ')
        if action == EXIT_COMMAND:
            break
        tax = 0
        if account > POOR_LEVEL:
            tax = tax_pay()
            print(f'Rich tax: {tax}')
        if action == ADD:
            amount_added = add_to_account()
            print(f'Amount added: {amount_added}')
        elif action == WITHDRAW:
            withdraw = withdraw_from_account()
            print(f'Amount withdrawn: {withdraw}')
        else:
            print(f'Wrong action: {action}')
        if count_operation == INTEREST_TIME:
            interest = calc_interest()
            print(f'Interest added: {interest}')
        print(f'Rich tax: {tax}')
        print(f'Account has: {account}')
    print('EXIT')


account: float = 0
commission = 0
count_operation = 0
operations: list = list()

start_operations()
