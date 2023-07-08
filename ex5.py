# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def calc_bonus(names: list, rates: list, bonus_rate: list):
    dict_bonuses: dict = dict()
    for name, rate, bonus in zip(names, rates, bonus_rate):
        bonus = bonus.replace('%', '')
        dict_bonuses[name] = rate * float(bonus) / 100
    return dict_bonuses


lst_names: list = ['Pifya', 'Smith', 'Neo']
lst_rate: list = [10, 11, 69]
lst_bonus_rate: list = ['10.50%', '34.44%', '69.96%']
bonuses = calc_bonus(lst_names, lst_rate, lst_bonus_rate)
print(f'Here goes the money {bonuses = }')
