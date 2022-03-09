class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        if self.num_cell - other.num_cell > 0:
            return Cell(self.num_cell - other.num_cell)
        else:
            print(f'Разность количества ячеек двух клеток меньше нуля')
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __floordiv__(self, other):
        if other.num_cell != 0:
            return Cell(self.num_cell // other.num_cell)
        else:
            print(f'Количество ячеек второй клетки равно нулю')
            return Cell(0)

    def __truediv__(self, other):
        if other.num_cell != 0:
            return Cell(round(self.num_cell / other.num_cell))
        else:
            print(f'Количество ячеек второй клетки равно нулю')
            return Cell(0)

    def make_order(self, row):
        for i in range(self.num_cell // row):
            print('*'*row)
        remain = self.num_cell % row
        if remain > 0:
            print('*'*remain)  # по заданию нужно убрать переход на новую строку, я оставил для красивого вывода


cell_1 = Cell(5)
cell_2 = Cell(4)

cell_3 = cell_1 + cell_2
print(cell_3.num_cell)
cell_3.make_order(4)

cell_3 = cell_1 - cell_2
print(cell_3.num_cell)

cell_3 = cell_2 - cell_1

cell_3 = cell_1 * cell_2
print(cell_3.num_cell)
cell_3.make_order(6)

cell_3 = cell_1 // cell_2
print(cell_3.num_cell)

cell_3 = cell_1 / cell_2
print(cell_3.num_cell)
