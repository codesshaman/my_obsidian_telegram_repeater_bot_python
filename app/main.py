import telebot
from model.config_parser import *
from controllers.routes import handlers
bot = telebot.TeleBot(parse_token())
bot.message_handler(commands=['start'])(handlers.start_handler)
bot.message_handler(commands=['health'])(handlers.health_handler)
bot.message_handler(commands=['help'])(handlers.help_handler)
bot.message_handler(commands=['text'])(handlers.text_handler)
if __name__ == '__main__':
    bot.polling(none_stop=True)
