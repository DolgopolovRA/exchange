import random


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(0, 0) for _ in range(N)] for _ in range(N)]
        self.init()

    def min_around(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine:
                    if i > 0:
                        self.pole[i - 1][j].around_mines += 1
                        if j > 0:
                            self.pole[i - 1][j - 1].around_mines += 1
                        if j < self.N-1:
                            self.pole[i - 1][j + 1].around_mines += 1
                    if j > 0:
                        self.pole[i][j - 1].around_mines += 1
                    if j < self.N-1:
                        self.pole[i][j + 1].around_mines += 1

                    if i < self.N-1:
                        self.pole[i + 1][j].around_mines += 1
                        if j > 0:
                            self.pole[i + 1][j - 1].around_mines += 1
                        if j < self.N-1:
                            self.pole[i + 1][j + 1].around_mines += 1

    def init(self):
        m = 0
        while m < self.M:
            x = random.randint(0, self.N-1)
            y = random.randint(0, self.N-1)
            if self.pole[x][y].mine == 0:
                self.pole[x][y].mine = 1
                m += 1
        self.min_around()

    def show(self):
        for el in self.pole:
            for cell in el:
                if cell.mine:
                    print('X', end=' ')
                else:
                    print(cell.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()
