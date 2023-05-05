import os
from model.config_parser import parse_folder


def dirscan():
    "Сканирование существующих папок"
    folder = parse_folder()
    result = os.scandir(folder)
    directories = []
    for item in result:
        if item.is_dir():
            directories.append(item)
    return directories


class Create:
    "Класс создания файлов и папок"
    def __init__(self, uri):
        super().__init__()

    def create_note():
        "Создание заметкий"
        return 'Создание заметки2'

    def create_category():
        "Создание категории"
        text = 'Создание категории'
        return text

    def create_subcategory():
        "Создание категории"
        text = 'Создание подкатегории'
        return text

    def create_folders():
        "Создание недостающих папок"
        dir = dirscan()
        folder = parse_folder()
        creation = True
        dirnames = ['categories', 'lists', 'notes', 'repeats']
        for elem in dirnames:
            if elem not in dir:
                new = os.path.join(folder, elem.encode('unicode-escape').decode())
                print(new)
                if not os.path.exists(new):
                    os.makedirs(new)
                    answer = "Папка " + dirname + " создана."
                else:
                    answer = "Папка " + dirname + " уже существует."
            else:
                answer = "Папка " + dirname + " уже существует."
        print(answer)
        return answer
