class ZeroDivision(Exception):
    def __init__(self, txt):
        self.text = txt


divisible = input('Введите делимое: ')
try:
    divider = input('Введите делитель: ')
    if int(divider) != 0:
        print(f'Результат деления: {float(divisible) / float(divider)}')
    else:
        raise ZeroDivision("Делитель не может равняться 0")
except ZeroDivision as zd:
    print(zd)
