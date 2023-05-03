from model.core.bot import bot
from model.file_module.scann import Scan
from telebot import types

keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('Ok', 'Bye')


@bot.message_handler(commands=['scan'])
def scan_handler(message):
    folder = Scan.scan()
    bot.send_message(message.chat.id, folder, parse_mode='HTML', reply_markup=keyboard1)
