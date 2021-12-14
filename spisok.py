'Задание a'
list_of_cubes = []
sum_list = 0
for i in range(0, 1000):
    if i % 2 != 0:
        list_of_cubes.append(i ** 3)

for element in list_of_cubes:
    sum_elements = 0
    i = 10
    cycle_element = element
    while cycle_element / i > 0:
        sum_elements = sum_elements + cycle_element % i
        cycle_element = cycle_element // i
    if sum_elements % 7 == 0:
        sum_list = sum_list + element

print(sum_list)

'Задание b'
index = 0
for element in list_of_cubes:
    list_of_cubes[index] = element + 17
    index += 1
    sum_elements = 0
    i = 10
    cycle_element = element
    while cycle_element / i > 0:
        sum_elements = sum_elements + cycle_element % i
        cycle_element = cycle_element // i
    if sum_elements % 7 == 0:
        sum_list = sum_list + element
print(sum_list)
