import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

command = sys.argv[1]
if command == 'list':
    get_list()
elif command == 'create_file':
    pass
elif command == 'create_folder':
    pass
