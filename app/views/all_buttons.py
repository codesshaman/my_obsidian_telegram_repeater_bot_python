from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

class Buttons:
    "Класс для отображения кнопок"
    def __init__(self, uri):
        super().__init__()
        self.uri = "https://apps.timwhitlock.info/emoji/tables/unicode"

    def main_set(lang):
        return u'🔧 Настройки' if lang == "ru" else u'🔧 Settings'

    def main_view(lang):
        return u'📋 Просмотр заметок' if lang == "ru" else u'📋 View notes'

    def main_cat(lang):
        return u'📝 Новая категория' if lang == "ru" else u'📝 New category'

    def main_note(lang):
        return u'📌 Новая заметка' if lang == "ru" else u'📌 New note'

    def set_rep(lang):
        return u'📅 Настройки повторений' if lang == "ru" else u'📅 Repeats settings'

    def set_lang(lang):
        return u'🌏 Язык приложения' if lang == "ru" else u'🌏 Application language'

    def set_help(lang):
        return u'❓ Справка' if lang == "ru" else u'❓ About'

    def set_back(lang):
        return u'↩ Назад' if lang == "ru" else u'↩ Back'