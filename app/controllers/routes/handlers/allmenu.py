# from controllers.routes.handlers import creation
# from controllers.routes.handlers import overview
# from controllers.routes.handlers import settings
from views.all_buttons import Buttons
from model.core.bot import bot, dp
from aiogram import types


main_menu = Buttons.main_menu()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
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
