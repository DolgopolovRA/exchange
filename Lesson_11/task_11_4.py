class WareHouse:
    pass


class OfficeEquip:
    def __init__(self, maker, color, year):
        self.maker = maker
        self.color = color
        self.year = year


class Printer(OfficeEquip):
    def __init__(self, maker, color, year, laser):
        super().__init__(maker, color, year)
        self.laser = laser


class Scanner(OfficeEquip):
    pass


class Xerox(OfficeEquip):
    pass

pr = Printer('Xerox', 'White', 2020, True)
print(pr.maker, pr.color, pr.year, pr.laser)