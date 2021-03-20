import os
import shutil
import my_project


root_dir = my_project.__path__[0]

for root, dirs, files in os.walk(root_dir):
    for dir in dirs:

        if 'templates' in dir:
            try:
                os.chdir(root_dir)
                shutil.copytree(os.path.join(root,'templates'), 'templates')
            except FileExistsError:
                os.chdir('templates')
                shutil.copytree(os.path.join(root, r'C:\Users\net\Desktop\pyton\LESSONS\lessons7\my_project\mainapp\templates\mainapp'), 'mainapp')








