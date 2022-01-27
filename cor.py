A = (1, 2, 3, 4, 5, 40)
B = (40, 1, 2, 3, 5, 8, 23, 4)
elem_not = True
for i in A:
    if B.count(i) > 0:
        continue
    else:
        elem_not = False;
if elem_not:
    print('Все элементы входят в кортеж В')
else:
    print('Не все элементы входят в кортеж В')
