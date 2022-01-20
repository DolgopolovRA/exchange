def thesaurus(*args):
    dict_f = {}

    for i in args:
        sp = dict_f.get(i[0], False)
        if sp:
            dict_f.update({i[0]: sp + [i]})
        else:
            dict_f.update({i[0]: [i]})

    return dict_f


def thesaurus_adv(*args):
    dict_f = {}

    for i in args:
        key = i[i.find(" ")+1]  # получаем ключ первой буквы фамилии
        dict_1 = dict_f.get(key, False)
        if dict_1:  # если получили словарь
            sp_in = dict_1.get(i[0], False)  # проверяем наличие ключа по первой букве имени
            if sp_in:  # если есть список
                dict_1.update({i[0]: sp_in + [i]})  # обновляем список
            else:
                dict_1.update({i[0]: [i]})  # создаём новый словарь
        else:  # нужно обновить словарь
            dict_f.update({key: {i[0]: [i]}})

    return dict_f


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Алексей"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
