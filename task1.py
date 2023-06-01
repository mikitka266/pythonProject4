'''Напишите функцию для транспонирования матрицы'''


def trans_matrix():
    matrix = [(1, 2, 3), (4, 5, 6)]
    trans = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans[j][i] = matrix[i][j]

    return trans


print(trans_matrix())
