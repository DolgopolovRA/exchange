import os
import shutil

root_dir, _ = os.path.split(os.path.abspath('task_7_3.py'))

for root, dirs, files in os.walk(root_dir):
    if root.endswith(r'\my_project'):
        exc_folder = os.path.join(root, 'templates')
        if not os.path.exists(exc_folder):
            os.mkdir(exc_folder)
    if root.endswith(r'\templates') and root != exc_folder:
        for d in dirs:
            if not os.path.exists(os.path.join(exc_folder, d)):
                shutil.copytree(os.path.join(root, d), os.path.join(exc_folder, d))
