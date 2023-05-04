from model.core.bot import bot
from model.file_module.scann import Scan
from telebot import types

keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('Ok', 'Bye')


@bot.message_handler(commands=['scan'])
def scan_handler(message):
    result = Scan.scan()
    folders = Scan.check_folders()
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    # keyboard = types.InlineKeyboardMarkup(row_width=2)
    if folders[0]:
        print('f0')
        keyboard.add(types.InlineKeyboardButton('создать папку повторений'))
    if folders[1]:
        print('f1')
        keyboard.add(types.InlineKeyboardButton('создать папку категорий'))
    if folders[2]:
        print('f2')
        keyboard.add(types.InlineKeyboardButton('создать папку списков'))
    if folders[3]:
        print('f3')
        keyboard.add(types.InlineKeyboardButton('создать папку заметок'))
    bot.send_message(message.chat.id,
                     result,
                     parse_mode='HTML',
                     reply_markup=keyboard)
