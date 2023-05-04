import os, re
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


class Scan:
    "Класс сканирования файловой системы"
    def __init__(self, uri):
        super().__init__()

    def scan():
        "Тестирование файловой системы"
        dir = dirscan()
        repeats = True if 'repeats' in dir else False
        cat = True if 'categories' in dir else False
        lists = True if 'lists' in dir else False
        notes = True if 'notes' in dir else False
        repansw = ' ' if repeats else '\nпапка для <b>повторений</b>.............. (создать)'
        repcat = ' ' if cat else '\nпапка для <b>категорий</b>................. (создать)'
        replists = ' ' if lists else '\nпапка для <b>списков заметок</b>.... (создать)'
        repnotes = ' ' if notes else '\nпапка для <b>заметок</b>.................... (создать)'
        answer = 'Все директории в порядке' if repeats and cat and lists and notes else 'Отсутствуют следующие директории:'
        return answer + repansw + repcat + replists + repnotes

    def check_folders():
        "Проверка отсутствия необходимых папок"
        dir = dirscan()
        answer = []
        answer.append(False) if 'repeats' in dir else answer.append(True)
        answer.append(False) if 'categories' in dir else answer.append(True)
        answer.append(False) if 'lists' in dir else answer.append(True)
        answer.append(False) if 'notes' in dir else answer.append(True)
        print(answer)
        return answer
    def scan_subsection():
        "Сканирование разделов"
        text = "Сканирую папку"
        return text