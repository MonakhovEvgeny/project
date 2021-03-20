import os


def create_folder(name):
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError:
        print(f'Папка с таким именем {name} уже существует')
        os.chdir(name)


def create_folder_in(name):
    for f in name:
        try:
            os.mkdir(f)
        except FileExistsError:
            print(f'Папка с таким именем {f} уже существует')



if __name__ == '__main__':

    create_folder('my_project')
    create_folder_in(['settings','mainapp', 'adminapp', 'authapp'])

