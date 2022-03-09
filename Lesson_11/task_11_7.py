class CompNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a != 0:
            if self.b < 0:
                return f'{self.a}{self.b}i'
            elif self.b > 0:
                return f'{self.a}+{self.b}i'
            else:
                return f'{self.a}'
        else:
            if self.b != 0:
                return f'{self.b}i'
            else:
                return 0

    def __add__(self, other):
        return CompNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return CompNum((self.a*other.a - self.b*other.b), (self.a*other.a + self.b*other.b))


z1 = CompNum(4, 7)
z2 = CompNum(-5, -4)
print(f'({z1}) + ({z2}) = {z1 + z2}')
print(f'({z1}) * ({z2}) = {z1 * z2}')
