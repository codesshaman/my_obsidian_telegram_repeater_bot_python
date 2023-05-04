from model.core.bot import bot
from controllers.routes.handlers import creation
from controllers.routes.handlers import handlers
from controllers.routes.handlers import scanning
from controllers.routes.handlers import settings
if __name__ == '__main__':
    bot.polling(none_stop=True)
