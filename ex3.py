# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def form_dict(text_numbers: str):
    lst_numbers = text_numbers.split()
    key = chr(int(lst_numbers[0]))
    value = int(lst_numbers[1])
    dict_num = {key: value}
    return dict_num


dict_num = form_dict('128521 382')
print(f'{dict_num = }')
