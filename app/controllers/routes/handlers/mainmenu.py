from controllers.routes.handlers import creation
# from controllers.routes.handlers import overview
# from controllers.routes.handlers import settings
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, CallbackQuery, CallbackData
from views.all_buttons import Buttons
from model.core.bot import bot, dp
from aiogram import types

#https://www.youtube.com/watch?v=D9RvmMxtOTI
lang = "ru"

m1 = Buttons.main_view(lang)
m2 = Buttons.main_note(lang)
m3 = Buttons.main_cat(lang)
m4 = Buttons.main_set(lang)
s1 = Buttons.set_rep(lang)
s2 = Buttons.set_lang(lang)
s3 = Buttons.set_help(lang)
s4 = Buttons.set_back(lang)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add(m1).insert(m2).add(m3).insert(m4)
sett = ReplyKeyboardMarkup(resize_keyboard=True)
sett.add(s1).insert(s2).add(s3).insert(s4)


@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.reply("Главное меню",  reply_markup=main)


@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    await message.reply("Меню настроек",  reply_markup=sett)


@dp.callback_query_handler(lambda c: c.data in [m1, m2, m3, m4])
async def handler(message: types.Message):
    try:
        print("Перешёл в обработчик меню")
        if message.text == m1:
            await message.answer("Просмотреть заметки")
        elif message.text == m2:
            await message.answer("Новая заметка")
        elif message.text == m3:
            await message.answer("Создание категории")
        elif message.text == m4:
            await settings(message)
    except Exception as e:
        print(e)


@dp.callback_query_handler(lambda c: c.data in [s1, s2, s3, s4])
async def settings_handler(message: types.Message):
    try:
        print("Перешёл в обработчик настроек")
        if message.text == s1:
            await message.answer("Настройки повторений")
        elif message.text == s2:
            await message.answer("Настройки языка")
        elif message.text == s3:
            await message.answer("Справка")
        elif message.text == s4:
            await main_menu(message)
    except Exception as e:
        print(e)

dp.register_message_handler(settings, commands=['settings'])
dp.register_message_handler(settings_handler)
dp.register_message_handler(main_menu, commands=['start'])
dp.register_message_handler(handler)
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
