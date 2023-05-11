from aiogram import Bot, Dispatcher
from model.config_parser import parse_token

bot = Bot(parse_token())
dp = Dispatcher(bot)