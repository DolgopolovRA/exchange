str_in = input('Введите строку: ')
num = 0
str_in = (str_in[::-1])
for i in range(0, len(str_in)):
    if str_in[i] == '1':
        num += 2 ** i


print(num)

