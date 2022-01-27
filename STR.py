"""
--------------------------------------
s = 'w'
sp = list(s)
dict_1 = {k: sp.count(k) for k in sp}
print(dict_1)
-------------------------------------
str_1 = input('str_1: ')
if len(str_1) > 1:
    str_res = f'{str_1[:2]}{str_1[-2:]}'
print(str_res)
-------------------------------------
str_1 = 'restart'
str_res = f'{str_1[0]}{str_1[1:].replace(str_1[0], "$")}'
print(str_res)
-------------------------------------
str_1, str_2 = 'abc', 'xyz'
str_res = f'{str_2[:2]}{str_1[2:]} {str_1[:2]}{str_2[2:]}'
print(str_res)
-------------------------------------
str_1 = input('Str_1: ')
if len(str_1) > 2:
    str_res = f'{str_1}ly' if str_1[-3:] == "ing" else f'{str_1}ing'
else:
    str_res = str_1
print(str_res)
-------------------------------------
"""
str_1 = input('Str_1: ')
