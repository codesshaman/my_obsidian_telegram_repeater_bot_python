from model.send_module.send import Send
from model.core.bot import bot
# from telebot import types
# keyboard1 = types.ReplyKeyboardMarkup()
# keyboard1.row('Ok', 'Bye')


@bot.message_handler(commands=['start'])
def start_handler(message):
    welcome = f'Здравствуй, товарищ <b>{message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, welcome, parse_mode='HTML', reply_markup=keyboard1)


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
