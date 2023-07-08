# Напишите функцию для транспонирования матрицы


def trans(matrix_traspond: list):
    trans_matrix: list = list()
    for i in range(len(matrix_traspond[0])):
        trans_matrix.append(list())
    for j in range(len(trans_matrix)):
        for i in range(len(matrix_traspond)):
            trans_matrix[j].append(matrix_traspond[i][j])
    return trans_matrix


def print_matrix(matrix_print: list):
    for lst in matrix_print:
        print(lst)


matrix: list = [[1, 2, 3], [4, 5, 6]]
print('Original matrix')
print_matrix(matrix)
matrix = trans(matrix)
print('Trans matrix')
print_matrix(matrix)
