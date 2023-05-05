from controllers.routes.handlers import allmenu
from model.file_module.setting import Set
from views.all_buttons import Buttons
from model.core.bot import bot
from telebot import types

settings_menu = Buttons.settings_menu()
back_button = Buttons.back_button()
settings_button = Buttons.settings_button()

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.chat.type == 'private':
        #####################################
        # Команды, приходящие из данного меню
        #####################################
        if message.text in settings_menu:
            if message.text == settings_menu[0]:
                repeats(message)
            if message.text == settings_menu[1]:
                folders(message)
            if message.text == settings_menu[2]:
                reference(message)
            if message.text == settings_menu[3]:
                allmenu.main_menu(message)
            ######################################
            # Команды, приходящие из главного меню
            ######################################
        else:
            if message.text == settings_button:
                settings(message)


@bot.message_handler(commands=['settings'])
def settings(message):
    print('Попал в меню настроек')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(settings_menu[0])
    item2 = types.KeyboardButton(settings_menu[1])
    item3 = types.KeyboardButton(settings_menu[2])
    item4 = types.KeyboardButton(settings_menu[3])
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

