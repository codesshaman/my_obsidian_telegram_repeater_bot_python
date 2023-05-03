import telebot
from model.config_parser import parse_token

bot = telebot.TeleBot(parse_token())