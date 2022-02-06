import os

dir_path = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for key, val in dir_path.items():
    if not os.path.exists(key):
        os.mkdir(key)
        for item in val:
            os.mkdir(os.path.join(key, item))
    else:
        for item in val:
            r_dir = os.path.join(key, item)
            if not os.path.exists(r_dir):
                os.mkdir(r_dir)
