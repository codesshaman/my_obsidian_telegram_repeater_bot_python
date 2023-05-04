from model.file_module.create import Create
from model.file_module.setting import Set
from model.file_module.scann import Scan
from model.send_module.send import Send
from model.core.bot import bot
from telebot import types


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('✍ Новая категория')
    item2 = types.KeyboardButton('✏ Новая заметка')
    item3 = types.KeyboardButton('📋 Просмотр заметок')
    item4 = types.KeyboardButton('⚙ Настройки')
    markup.add(item1, item2, item3, item4)
    welcome = f'Здравствуй, товарищ <b>{message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, welcome, parse_mode='HTML', reply_markup = markup)

# https://www.youtube.com/watch?v=A1p7bEtTlxc

@bot.message_handler(commands=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '✍ Новая категория':
            answer = Create.create_category()
            bot.send_message(message.chat.id, answer)
        elif message.text == '✏ Новая заметка':
            answer = Create.create_note()
            bot.send_message(message.chat.id, answer)
        elif message.text == '📋 Просмотр заметок':
            answer = Scan.scan_subsection()
            bot.send_message(message.chat.id, answer)
        elif message.text == '⚙ Настройки':
            answer = Set.settings_menu()
            bot.send_message(message.chat.id, answer)
@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, 'Справка')


@bot.message_handler(commands=['send'])
def help_handler(message):
    msg = Send.send_message()
    bot.send_message(message.chat.id, msg)


# @bot.message_handler(func=lambda message: True)
# def send_text(message):
#     if message.text.lower() == 'Hello':
#         bot.send_message(message.chat.id, message.text.upper() )
#     elif message.text.lower() == 'Bye':
#         bot.send_message(message.chat.id,'see you soon' )
#     elif message.text.lower() == 'I love you':
#         bot.send_sticker(message.chat.id, 'sticker_id')

# @bot.message_handler(content_types=['sticker'])
# def sticker_id(message):
#     print(message)
