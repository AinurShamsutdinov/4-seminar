# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
#   и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
#   прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def calc_profit(companies: dict):
    for companies, balance in companies.items():
        if sum(balance) < 0:
            return False
    return True


dict_companies = {
                    'Audi': [0, 10, 39, 329, -23, -2348, 484, 2994, 29, 92],
                    'Lotus': [39, 39, -23, 48, 4, 24, 2, 92],
                    'VW Group': [10, 3, 29],
                    'BMW': [0, 39, 3, -23, 4, 224, 859, 92],
                    'Mercedes': [39, 129, 384, 454, 29, 92],
                    'AutoVAZ': [-39, -129, -384, -454, -29, -92]
                }
profitability: bool = calc_profit(dict_companies)
print(f'Companies are profitable {profitability}')
