class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        res_sum = [[i + j for i, j in zip(el_1, el_2)] for el_1, el_2 in zip(self.matrix, other.matrix)]
        return Matrix(res_sum)

    def __str__(self):
        for i in self.matrix:
            print(*i)
        return ''


m1 = Matrix([[10, 252], [3.25, 45], [75, 69]])
m2 = Matrix([[1.5, 42], [32, 425], [52, 623]])
m3 = Matrix([[1, 2], [3, 4], [5, 6]])
res = m1 + m2 + m3
print(m2)
print(res)

