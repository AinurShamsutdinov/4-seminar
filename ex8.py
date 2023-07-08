#   Задание №8
#
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
#   оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

import sys

MODULE = sys.modules[__name__]


def create_variable(text: str):
    length = len(text)
    global_var: dict = globals()
    if text[length - 1] == 's':
        name = text[:length - 1]
        setattr(MODULE, name, str())
        for key, var in global_var.items():
            if var == text:
                globals()[key] = None


text_1 = 'var_1s'
text_2 = 'var_2s'
text_3 = 'var_3'
text_4 = 'var_4s'
text_5 = 'var_5s'
text_6 = 'var_6s'
list_variables = (text_1, text_2, text_3, text_4, text_5, text_6)

create_variable(text_1)
create_variable(text_2)
create_variable(text_3)
create_variable(text_4)
create_variable(text_5)
create_variable(text_6)

global_variables: dict = globals().copy()
for key, var in global_variables.items():
    if (key + 's') in list_variables:
        print(f'{key} = {var}')

print(f'{text_1 = }')
print(f'{text_2 = }')
print(f'{text_3 = }')
print(f'{text_4 = }')
print(f'{text_5 = }')
