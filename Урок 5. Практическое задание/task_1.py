"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections

companies = collections.namedtuple('company', ['name', 'profit'])
dct_companies = {}
for _ in range(int(input('Введите количество предприятий для расчета прибыли: '))):
    companies.name = input('Введите название предприятия: ')
    companies.profit = tuple(map(int, input('введите прибыль данного предприятия: ').split()))
    print(companies.name, companies.profit)
    dct_companies[companies.name] = companies.profit

mid_profit = sum(map(sum, dct_companies.values())) / len(dct_companies)
down_mid_profit = list(k for k, v in dct_companies.items() if sum(v) < mid_profit)
up_mid_profit = list(k for k, v in dct_companies.items() if sum(v) > mid_profit)

print(f'Средняя годовая прибыль всех предприятий: {mid_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(up_mid_profit)}')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(down_mid_profit)}')
