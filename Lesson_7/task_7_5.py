import os
import json

root_dir, _ = os.path.split(os.path.abspath('task_7_4.py'))
dict_res = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key = f'1'.ljust(len(str(size))+1, '0')
        val = dict_res.get(key)
        if len(file.split('.')) > 1:
            ext = file.split('.')[-1]
        else:
            ext = ''
        if val is not None:
            if val[1].count(ext) == 0:
                val[1].append(ext)
            dict_res[key] = [str(int(val[0]) + 1), val[1]]
        else:
            dict_res.setdefault(key, ['1', [ext]])
for k, v in dict_res.items():
    dict_res.update({k: tuple(v)})
_, way = os.path.split(root_dir)
with open(way + '_summary.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(dict_res))
