lst_in = "Пушкин: Сказака о рыбаке и рыбке\nЕсенин: Письмо к женщине\nТургенев: Муму\nПушкин: Евгений Онегин\nЕсенин: Русь".split('\n')
print(lst_in)
d = {}
for el in lst_in:
    k, v = el.split(': ')
    if d.get(k):
        d[k].add(v)
    else:
        d[k] = {v}
d = {el.split(': ')[0]: {el.split(': ')[1]} for el in lst_in if d}
print(d)

