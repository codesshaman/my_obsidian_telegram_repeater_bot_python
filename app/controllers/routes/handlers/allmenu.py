# from controllers.routes.handlers import creation
# from controllers.routes.handlers import overview
# from controllers.routes.handlers import settings
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from views.all_buttons import Buttons
from model.core.bot import bot, dp
from aiogram import types

#https://www.youtube.com/watch?v=D9RvmMxtOTI

main_menu = Buttons.main_menu()
b1 = KeyboardButton(main_menu[0])
b2 = KeyboardButton(main_menu[1])
b3 = KeyboardButton(main_menu[2])
b4 = KeyboardButton(main_menu[3])
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(b1).insert(b2).add(b3).insert(b4)


@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.reply("Главное меню",  reply_markup=markup)


async def main_menu_handler(message: types.Message):
    try:
        if message.text == main_menu[0]:
            await message.answer("Просмотр заметок")
        elif message.text == main_menu[1]:
            await message.answer("Создание категории")
        elif message.text == main_menu[2]:
            await message.answer("Создание заметки")
        elif message.text == main_menu[3]:
            await message.answer("Настройки")
    except Exception as e:
        print(e)

dp.register_message_handler(main_menu, commands=['start'])
dp.register_message_handler(main_menu_handler)
# dp.register_message_handler(main_menu_handler, commands=['start'])
#
# @bot.message_handler(commands=['start'])
# def main_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton(main_menu[0])
#     item2 = types.KeyboardButton(main_menu[1])
#     item3 = types.KeyboardButton(main_menu[2])
#     item4 = types.KeyboardButton(main_menu[3])
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'Главное меню бота', reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def nested_first(message):
#     if message.chat.type == 'private':
#         if message.text == main_menu[0]:
#             overview.handler(message)
#         elif message.text == main_menu[1]:
#             creation.handler(message)
#         elif message.text == main_menu[2]:
#             creation.handler(message)
#         elif message.text == main_menu[3]:
#             settings.handler(message)
#         elif message.text == '⬅ Назад':
#             main_menu(message)
