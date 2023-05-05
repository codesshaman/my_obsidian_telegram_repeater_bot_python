from model.core.bot import bot
from controllers.routes.handlers import allmenu
if __name__ == '__main__':
    bot.polling(none_stop=True)
