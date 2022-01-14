list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0

while index < len(list_1):
    elem = list_1[index]
    number = 0  # изначально считаем что это не число
    len_number = 0  # длина числа
    sign = 0  # признак числа со знаком
    for i in range(len(elem)):
        if 48 <= ord(elem[i]) <= 57:
            number = 1
            len_number += 1
        elif ord(elem[i]) == 43 or ord(elem[i]) == 45:
            sign = 1
        else:
            number = 0
            break
    if number:
        if len_number < 2:
            if sign:
                list_1[index] = elem[0] + '0' + elem[1]
            else:
                list_1[index] = '0' + elem
        list_1.insert(index, '"')
        list_1.insert(index + 2, '"')
        index += 2
    else:
        index += 1

print(list_1)
