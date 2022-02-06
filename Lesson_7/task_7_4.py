import os

root_dir, _ = os.path.split(os.path.abspath('task_7_4.py'))
dict_res = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key = f'1'.ljust(len(str(size))+1, '0')
        val = dict_res.get(key)
        if val is not None:
            dict_res[key] = val + 1
        else:
            dict_res.setdefault(key, 1)
print(dict_res)
