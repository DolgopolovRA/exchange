import yaml
import os


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
