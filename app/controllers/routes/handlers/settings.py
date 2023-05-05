from controllers.routes.handlers import allmenu
from model.file_module.setting import Set
from model.core.bot import bot
from telebot import types


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.chat.type == 'private':
        print('Попал в обработчик настроек')
        ######################################
        # Команды, приходящие из главного меню
        ######################################
        if message.text == '⚙ Настройки':
            print('Выбрал нужный if')
            settings(message)
        #####################################
        # Команды, приходящие из данного меню
        #####################################
        if message.text == '🗓 Настройка повторений':
            repeats(message)
        if message.text == '📁 Проверка папок':
            folders(message)
        if message.text == '❓ Справка':
            reference(message)
        if message.text == '⬅ Назад':
            allmenu.main_menu(message)


@bot.message_handler(commands=['settings'])
def settings(message):
    print('Попал в меню настроек')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'🗓 Настройка повторений')
    item2 = types.KeyboardButton(u'📁 Проверка папок')
    item3 = types.KeyboardButton(u'❓ Справка')
    item4 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню настроек', reply_markup=markup)

@bot.message_handler(commands=['rep'])
def repeats(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'🗓 Настройки повторений')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = 'Настройки повторений'
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['folders'])
def folders(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'📁 Проверить директории')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = 'Проверить директории'
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['reference'])
def reference(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'❓ Справка о программе')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = '❓ Справка'
    bot.send_message(message.chat.id, answer, reply_markup=markup)

