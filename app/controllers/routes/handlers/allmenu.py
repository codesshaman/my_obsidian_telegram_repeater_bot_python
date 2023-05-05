from controllers.routes.handlers import creation
from controllers.routes.handlers import overview
from controllers.routes.handlers import settings
from model.core.bot import bot
from telebot import types


@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('✍ Новая категория')
    item2 = types.KeyboardButton('✏ Новая заметка')
    item3 = types.KeyboardButton('📋 Просмотр заметок')
    item4 = types.KeyboardButton('⚙ Настройки')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Главное меню бота', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def nested_first(message):
    if message.chat.type == 'private':
        if message.text == '✍ Новая категория':
            creation.handler(message)
        elif message.text == '✏ Новая заметка':
            creation.handler(message)
        elif message.text == '📋 Просмотр заметок':
            overview.handler(message)
        elif message.text == '⚙ Настройки':
            print("Нажал на handler")
            settings.handler(message)
        elif message.text == '⬅ Назад':
            main_menu(message)
