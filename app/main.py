from model.core.bot import bot, dp
from aiogram import executor
from controllers.routes.handlers import allmenu
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # bot.polling(none_stop=True)
