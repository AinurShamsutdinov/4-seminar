# a = 42
# print(type(a), id(a))
# print(type(id))
#
# very_bad_programming_style = sum
# print(very_bad_programming_style([1, 2, 3]))
######################################################################################
# def my_func():
#     pass
######################################################################################
# def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return None
#
# print(quadratic_equations(2, -3, -9))
#####################################################################################
def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }')    # Для демонстрации работы, но не для привычки принтить из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')
#####################################################################################
