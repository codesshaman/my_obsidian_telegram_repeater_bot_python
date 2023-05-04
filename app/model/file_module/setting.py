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


class Set:
    "Класс обработки меню настроек"
    def __init__(self, uri):
        super().__init__()

    def settings_menu():
        "Настройки программы"
        text = "Настройки программы"
        return text

    def help_menu():
        "Справка о программе"
        text = "Справка о программе"
        return text


