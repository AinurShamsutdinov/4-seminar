# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def form_unicode_list(text):
    char_list = list(text)
    letter_set = set(char_list)
    char_list = list(map(lambda x: ord(x), letter_set))
    sorted_descending_list = list(reversed(sorted(char_list)))
    return sorted_descending_list


text = '# Задание №2' \
        '# ✔ Напишите функцию, которая принимает строку текста. ' \
        '# ✔ Сформируйте список с уникальными кодами Unicode каждого ' \
        '# символа введённой строки отсортированный по убыванию.'
print(form_unicode_list(text))
