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
str_1 = input('Str_1: ')


def long_str(s):
    len_s = 0
    sp = s.split(' ')
    for i in sp:
        if len(i) > len_s:
            len_s = len(i)
    return len_s


print(long_str(str_1))
-------------------------------------
str_1 = input('Str_1: ')
print(f'{str_1[-1]}{str_1[1:-1]}{str_1[0]}')
-------------------------------------
str_1 = input('Str_1: ')


def odd_val_str(s):
    str_r = ''
    sp = [s[i] for i in range(len(s)) if i % 2 == 0]
    return str_r.join(sp)


print(odd_val_str(str_1))
-------------------------------------
str_1 = input('Str_1: ')

numbers = {w: str_1.count(w) for w in str_1.split()}
print(numbers)
-------------------------------------
str_1 = input('Str_1: ')
print(str_1.upper())
print(str_1.lower())
-------------------------------------
str_1 = input('Str_1: ')
s = ''
sp = [i.lower().rstrip('.') for i in str_1.split()]
print(' '.join(sorted(set(sp))))
"""
# 14 задача по строкам