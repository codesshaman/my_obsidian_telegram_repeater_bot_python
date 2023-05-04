from model.core.bot import bot
from model.file_module.scann import Scan
from model.file_module.create import Create
from telebot import types

keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('Ok', 'Bye')


@bot.message_handler(commands=['scan'])
def scan_handler(message):
    result = Scan.scan()
    result = Scan.check_folders()
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    callback = 'normal'
    if not result:
        keyboard.add(types.InlineKeyboardButton('создать папки'))
        callback = 'create'
    # if folders[1]:
    #     keyboard.add(types.InlineKeyboardButton('создать папку категорий'))
    # if folders[2]:
    #     keyboard.add(types.InlineKeyboardButton('создать папку списков'))
    # if folders[3]:
    #     keyboard.add(types.InlineKeyboardButton('создать папку заметок'))
    bot.send_message(message.chat.id,
                     result,
                     parse_mode='HTML',
                     reply_markup=keyboard,
                     callback_data=str(callback))

@bot.callback_query_handler(func=lambda callback: True)
def callback_answer(callback):
    print("вход в обработчик")
    if callback.data == 'create':
        print("обработчик")
        Create.create_folders()
