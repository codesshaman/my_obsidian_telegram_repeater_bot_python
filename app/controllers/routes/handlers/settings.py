from controllers.routes.handlers import mainmenu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from views.all_buttons import Buttons
from model.core.bot import bot, dp
from aiogram import types

lang = "ru"

b1 = Buttons.set_rep(lang)
b2 = Buttons.set_lang(lang)
b3 = Buttons.set_help(lang)
b4 = Buttons.set_back(lang)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(b1).insert(b2).add(b3).insert(b4)


@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    await message.reply("Меню настроек",  reply_markup=markup)


async def settings_handler(message: types.Message):
    try:
        if message.text == b1:
            await message.answer("Настройки повторений")
        elif message.text == b2:
            await message.answer("Настройки языка")
        elif message.text == b3:
            await message.answer("Справка")
        elif message.text == b4:
            mainmenu.handler(message)
    except Exception as e:
        print(e)

dp.register_message_handler(settings, commands=['settings'])
dp.register_message_handler(settings_handler)