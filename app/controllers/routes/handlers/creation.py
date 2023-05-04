from model.core.bot import bot
from telebot import types


@bot.message_handler(commands=['create_'])
def start_handler(message):
    welcome = f'Здравствуй, товарищ <b>{message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, welcome, parse_mode='HTML', reply_markup=keyboard1)
