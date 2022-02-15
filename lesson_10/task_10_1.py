class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        res_sum = [[i + j for i, j in zip(el_1, el_2)] for el_1, el_2 in zip(self.matrix, other.matrix)]
        return Matrix(res_sum)

    def __str__(self):
        for i in self.matrix:
            print(*i)
        return ''


m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[1.5, 2], [3, 4], [5, 6]])
m3 = Matrix([[1, 2], [3, 4], [5, 6]])
try:
    res = m1 + m2 + m3
    print(res)
    print(m3)
except ValueError:
    print('Сложение невозможно, матрицы разной размерности!')
