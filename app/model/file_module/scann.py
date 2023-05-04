import os
from model.config_parser import parse_folder


class Scan:
    "Класс для функций, индексирующих файлы"
    def __init__(self, uri):
        super().__init__()

    def scan():
        "Сканирование разделов"
        folder = parse_folder()
        result = os.scandir(folder)
        print("Сканирую папку " + folder)

        return str(result)

    def scan_section():
        "Сканирование разделов"
        text = "Сканирую папку"
        return text

    def scan_subsection():
        "Сканирование разделов"
        text = "Сканирую папку"
        return text