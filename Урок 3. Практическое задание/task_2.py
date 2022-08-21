"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api


from hashlib import pbkdf2_hmac
import psycopg2
from os import urandom


def ret_psw_hash(password, salt):
    psw_hash = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    return psw_hash.hex()


_salt = urandom(32)
print(_salt.hex())
psw = input('Введите пароль: ')
try:
    connect_db = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', port='5432', database='testdb')
    cursor = connect_db.cursor()
    cursor.execute('INSERT INTO psw(user, hash) VALUES (%s, %s)', ('user_1', ret_psw_hash(psw, _salt)))
    connect_db.commit()
    cursor.close()
    connect_db.close()

except Exception as err:
    print("Ошибка при работе с БД PostgreSQL", err)
"""

import json
from hashlib import pbkdf2_hmac
from os import urandom


def ret_psw_hash(password, salt):
    psw_hash = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    return psw_hash.hex()


_salt = urandom(32)
psw_1 = input('Введите пароль: ')
with open('psw.json', 'w') as psw_file:
    json.dump(ret_psw_hash(psw_1, _salt), psw_file)

psw_2 = input('Введите пароль ещё раз: ')
with open('psw.json', 'r') as psw_file:
    if json.load(psw_file) == ret_psw_hash(psw_2, _salt):
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')
