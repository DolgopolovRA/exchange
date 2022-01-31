"""
-------------------------------------
str_1 = (input('List_1: '))
res_sum = 0
res_mul = 1
for i in str_1.split():
    res_sum += int(i)
    res_mul *= int(i)
print(res_sum, res_mul)
-------------------------------------
str_1 = (input('List_1: '))

sp = list(map(int, str_1.split()))
sp.sort()
print(sp[-1])
print(sp[0])
-------------------------------------
list_1 = [(2, 5), (2, 0), (1, 2), (4, 4), (2, 3), (2, 1)]
list_1.sort(key=lambda x: x[-1])
print(list_1)
-------------------------------------
"""
str_1 = (input('List_1: '))
list_1 = list(set(str_1.split(',')))
# for i in list_1[:]:
#     if list_1.count(i) > 1:
#         list_1.remove(i)
# list_1 = list(set(list_1))
print(list_1)
