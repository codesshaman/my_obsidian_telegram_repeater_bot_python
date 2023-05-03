import telebot
from model.send_module.send import *
from model.config_parser import *
bot = telebot.TeleBot(parse_token())


@bot.message_handler(commands=['start'])
def start_handler(message):
    welcome = f'Здравствуй, товарищ <b>{message.from_user.last_name}</b>!'
    bot.send_message(message.chat.id, welcome, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, 'Справка')


@bot.message_handler(commands=['text'])
def text_handler(message):
    text = Send.send_message()
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def health_handler(message):
    bot.send_message(message.chat.id, 'Я здоров!')