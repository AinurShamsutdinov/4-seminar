# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def sort_nums(lst_nums: list):
    for i in range(len(lst_nums)):
        for j in range(len(lst_nums)):
            if lst_nums[i] < lst_nums[j]:
                buff = lst_nums[j]
                lst_nums[j] = lst_nums[i]
                lst_nums[i] = buff
    return lst_nums


lst_nums: list = [3, 5, 6, 7, 21, 39, 5, 30, 4, 5, 1, 9, 2, 59]
print(f'{lst_nums = }')
sort_nums(lst_nums)
print(f'{lst_nums = }')
