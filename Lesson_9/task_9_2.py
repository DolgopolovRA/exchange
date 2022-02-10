class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        mass = self._length * self._width * 125 / 1000
        return mass


road_1 = Road(20, 5000)
res_mass = road_1.calc()
print(res_mass)
