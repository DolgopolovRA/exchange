class WareHouse:
    @staticmethod
    def reception(el, num):
        if type(el) is Printer:
            atr = ('Принтер', el.maker, el.color, el.year, el.laser)
        elif type(el) is Scanner:
            atr = ('Сканер', el.maker, el.color, el.year, el.ccd)
        elif type(el) is Xerox:
            atr = ('Ксерокс', el.maker, el.color, el.year, el.colored)
        k = int(equip_wh.get(atr, 0))
        if k == 0:
            equip_wh.setdefault(atr, int(num))
        else:
            equip_wh.update({atr: int(num) + k})

    @staticmethod
    def remains_wh():
        if equip_wh == {}:
            print("Склад пуст!")
            input('Нажмите Enter для продолжения...')
        else:
            for i, j in equip_wh.items():
                if i[0] == 'Принтер':
                    lsr = ''
                    if i[4]:
                        lsr = 'Тип: лазерный. '
                    print(f'{i[0]} {i[1]}. {lsr}Цвет: {i[2]} Год: {i[3]} Количество: {j} шт.')
                elif i[0] == 'Сканер':
                    ccd = ''
                    if i[4]:
                        ccd = 'Технология CCD. '
                    print(f'{i[0]} {i[1]}. {ccd}Цвет: {i[2]} Год: {i[3]} Количество: {j} шт.')
                elif i[0] == 'Ксерокс':
                    clrs = ''
                    if i[4]:
                        clrs = 'Тип: цветной.'
                    print(f'{i[0]} {i[1]}. {clrs}Цвет: {i[2]} Год: {i[3]} Количество: {j} шт.')

    @staticmethod
    def relocate_wh(el, num):
        if type(el) is Printer:
            atr = ('Принтер', el.maker, el.color, el.year, el.laser)
        elif type(el) is Scanner:
            atr = ('Сканер', el.maker, el.color, el.year, el.ccd)
        elif type(el) is Xerox:
            atr = ('Ксерокс', el.maker, el.color, el.year, el.colored)
        k = int(equip_wh.get(atr, 0))
        if k == 0:
            print('Такого товара на складе нет!')
            return 0
        else:
            if k < int(num):
                print('На складе нет необходимого количества товара!')
                return 0
            else:
                equip_wh.update({atr: k - int(num)})


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
    def __init__(self, maker, color, year, ccd):
        super().__init__(maker, color, year)
        self.ccd = ccd


class Xerox(OfficeEquip):
    def __init__(self, maker, color, year, colored):
        super().__init__(maker, color, year)
        self.colored = colored


def val_err():
    print('выберите один из возможных вариантов!')
    input('Нажмите Enter для продолжения...')


def atr_err(atr):
    if atr.isdigit():
        if 0 <= int(atr) <= 1:
            return 1
        else:
            return 0
    else:
        return 0


equip_wh = {}
while True:
    command = input('Выберите действие:\n1 - добавить оргтехнику на склад\n2 - переместить со склада'
                    '\n3 - показать остатки на складе\n4 - выйти\n--> ')
    if command.isdigit():
        _command = int(command)
        if _command <= 0 or _command > 4:
            val_err()
            continue
    else:
        val_err()
        continue
    if _command == 1:
        type_org = input('Выберите тип оргтехники:\n1 - принтер\n2 - сканер\n3 - ксерокс\n--> ')
        if type_org.isdigit():
            _type_org = int(type_org)
            if _type_org <= 0 or _type_org > 4:
                val_err()
                continue
        else:
            val_err()
            continue
        mkr = input('Введите производителя: ')
        clr = input('Введите цвет: ')
        if not clr.isalpha():
            print('Цвет должен состоять только из букв!')
            input('Нажмите любую клавишу для продолжения...')
            continue
        yr = input('Введите год:')
        if not yr.isdigit():
            print('Год должен состоять только из цифр!')
            input('Нажмите любую клавишу для продолжения...')
            continue
        count = input('Введите количество: ')
        if not count.isdigit():
            print('Количество должно состоять только из целых цифр!')
            input('Нажмите любую клавишу для продолжения...')
            continue

        if _type_org == 1:
            _type = input('Принтер лазерный? 1 - да, 0 - нет\n')
            if atr_err(_type):
                WareHouse.reception(Printer(mkr, clr, yr, bool(int(_type))), count)
            else:
                val_err()
                continue

        elif _type_org == 2:
            _type = input('Сканер CCD? 1 - да, 0 - нет\n')
            if atr_err(_type):
                WareHouse.reception(Scanner(mkr, clr, yr, bool(int(_type))), count)
            else:
                val_err()
                continue

        elif _type_org == 3:
            _type = input('Ксерокс цветной? 1 - да, 0 - нет\n')
            if atr_err(_type):
                WareHouse.reception(Xerox(mkr, clr, yr, bool(int(_type))), count)
            else:
                val_err()
                continue

    elif _command == 2:
        crt = tuple(enumerate(equip_wh, start=1))
        for i, j in crt:
            print(f'{i} - {j}')
        num_el = input('Выберите товар из списка для перемещения: ')
        # здесь доработать передачу элемента для перемещения


    elif _command == 3:
        WareHouse.remains_wh()

    elif _command == 4:
        break
    else:
        print('выберите один из возможных вариантов!')
        input('Нажмите любую клавишу для продолжения...')
        continue
