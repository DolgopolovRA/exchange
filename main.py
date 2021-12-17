import os
import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir

save_info('старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствует команда')
else:

    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует имя файла/папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует имя файла/папки для копирования')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('help - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - смена директории')

    elif command == 'change_dir':
        try:
            new_path = sys.argv[2]
        except IndexError:
            print('Укажите директорию для перехода')
        else:
            change_dir(new_path)
            print(os.getcwd())


save_info('конец')
