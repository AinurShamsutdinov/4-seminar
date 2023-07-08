# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
#   до конца и/или начала списка.


def sum_numbers(list_numbers: list, beg: int, end: int):
    list_of_range: list = list()
    sum_of_nums = int()
    if beg < 0 & end < len(list_numbers):
        list_of_range = list_numbers[:end]
    elif beg < 0 & end > len(list_numbers):
        list_of_range = list_numbers[:]
    elif beg > 0 & end > len(list_numbers):
        list_of_range = list_numbers[beg:]
    elif beg > 0 & end < len(list_numbers):
        list_of_range = list_numbers[beg:end]
    for item in list_of_range:
        sum_of_nums += item
    return sum_of_nums


list_nums = [3, 4, 5, 6, 1, 3, 1, 7, 4, 7, 2, 52, 9, 93, 2, 5, 7, 1, 7]
sum_num = sum_numbers(list_nums, -13, 15)
print(f'{sum_num = }')
