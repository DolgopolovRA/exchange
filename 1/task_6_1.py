from operator import itemgetter

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    result = [itemgetter(0, 5, 6)(str_1.replace('"', '').split(' ')) for str_1 in file_1]

print(result[:3])  # срез из 3 элементов, чтобы убедиться что это действительно список кортежей нужного вида
