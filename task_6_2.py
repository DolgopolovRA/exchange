from operator import itemgetter
import collections

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    result = [itemgetter(0, 5, 6)(str_1.replace('"', '').split(' ')) for str_1 in file_1]
spam = collections.Counter(result).most_common(1)
print(f'IP спаммера: {spam[0][0][0]}, количество запросов: {spam[0][1]}')
