class Buttons:
    "Класс для отображения кнопок"
    def __init__(self, uri):
        super().__init__()

    @staticmethod
    def main_menu():
        menu = [
            u'📋 Просмотр заметок',
            u'✍ Новая категория',
            u'✏ Новая заметка',
            u'⚙ Настройки'
        ]
        return menu

    @staticmethod
    def settings_menu():
        menu = [
            u'🗓 Настройка повторений',
            u'📁 Проверка папок',
            u'❓ Справка',
            u'⬅ Назад'
        ]
        return menu

    @staticmethod
    def back_button():
        bb = u'⬅ Назад'
        return bb

    @staticmethod
    def settings_button():
        sb = '⚙ Настройки'
        return sb