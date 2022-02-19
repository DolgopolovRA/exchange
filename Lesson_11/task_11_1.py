import re


class Date:
    def __init__(self, date_str):
        self.date = date_str
        self.str_to_int(date_str)

    @classmethod
    def str_to_int(cls, date):
        da = re.findall(r'^\d\d-\d\d-\d{4}$', date)
        if not da:
            print('Неверный формат даты!')
        else:
            d, m, g = map(int, da[0].split('-'))
            cls.valid_date(d, m, g)

    @staticmethod
    def valid_date(d, m, g):
        if d == 0 or d > 31:
            print('Число должно быть больше 0 и меньше 32!')
        if m == 0 or m > 12:
            print('Месяц должен быть больше 0 и меньше 13!')
        if g == 0:
            print('Год должен быть больше 0!')


dt = Date(input('Введите дату в формате ДД-ММ-ГГГГ: '))
