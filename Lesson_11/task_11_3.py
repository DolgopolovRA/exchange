import re


class NumbersOnly(Exception):

    @staticmethod
    def check_num(elem):
        if re.findall(r'^[-\d\.]+$', elem):
            sp_num.append(elem)
        else:
            raise NumbersOnly


sp_num = []
while True:
    el = input('Введите число: ')
    if el == 'stop':
        print(sp_num)
        break
    else:
        try:
            NumbersOnly.check_num(el)
        except NumbersOnly:
            print('Нужно вводить только числа!')
            continue
