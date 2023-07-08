# 2
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def get_key_value_dict(key_find):
    global_dict = globals()
    dct_value = dict()
    for key_value, item_value in global_dict.items():
        if key_value == key_find:
            if item_value.__hash__ is not None:
                dct_value[item_value] = key_value
            else:
                dct_value[str(item_value)] = key_value
    return dct_value


text = 'Hello World!'
list_test = list()
key_of_text = str()
key_of_list = str()
global_dict: dict = dict(globals())

for key, item in global_dict.items():
    if item == text:
        key_of_text = key
    if item == list_test:
        key_of_list = key

dicti = get_key_value_dict(key_of_text)
dicti.update(get_key_value_dict(key_of_list))
for key, item in dicti.items():
    print(f'{key = }\t{item = }')
