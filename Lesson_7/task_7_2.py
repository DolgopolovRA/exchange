import yaml
import os


<<<<<<< Updated upstream
def create_struct(data, way):
    if isinstance(data, dict):
        for key, val in data.items():
            if not os.path.exists(os.path.join(way, key)):
                os.mkdir(os.path.join(way, key))
            way = os.path.join(way, key)
            way = create_struct(val, way)
    else:
        for elem in data:
            if isinstance(elem, dict):
                create_struct(elem, way)
            else:
                with open(os.path.join(way, elem), 'a', encoding='utf-8'):
                    pass
        way, _ = os.path.split(way)
        return way


with open('config.yaml', 'r', encoding='utf-8') as r:
    content = yaml.load(r, Loader=yaml.FullLoader)
start_way, _ = os.path.split(os.path.abspath('task_7_2.py'))
create_struct(content, start_way)
=======
def dict_r(dict_f):
    out_key = ''
    for key, val in dict_f.items():
        if isinstance(val, dict):
            print('вызов')
            out_key = out_key + val
            dict_r(val)
        else:
            out_val = val
    print(out_key)
    print(out_val)


with open('config.yaml', 'r', encoding='utf-8') as rf:
    content = yaml.load(rf, Loader=yaml.FullLoader)
# dict.
result = dict_r(content)
print(result)
# if isinstance(content, dict):
#     for key, val in content.items():
#         if not os.path.exists(key):
#             os.mkdir(key)
#         if isinstance(val, dict):
#             for key_1, val_1 in val.items():
#                 if not os.path.exists(key_1):
#                     os.mkdir(key_1)
#                 if isinstance(val, dict):
>>>>>>> Stashed changes
