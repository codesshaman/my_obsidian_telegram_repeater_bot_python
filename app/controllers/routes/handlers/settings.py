from controllers.routes.handlers import allmenu
from model.file_module.setting import Set
from model.core.bot import bot
from telebot import types


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.chat.type == 'private':
        print('Попал в обработчик настроек')
        ######################################
        # Команды, приходящие из главного меню
        ######################################
        if message.text == '⚙ Настройки':
            print('Выбрал нужный if')
            settings(message)
        #####################################
        # Команды, приходящие из данного меню
        #####################################
        if message.text == '🗓 Настройка повторений':
            choose_category(message)
        if message.text == '📁 Проверка папок':
            create_cat(message)
        if message.text == '❓ Справка':
            create_sub(message)
        if message.text == '⬅ Назад':
            allmenu.main_menu(message)


@bot.message_handler(commands=['settings'])
def settings(message):
    print('Попал в меню настроек')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🗓 Настройка повторений')
    item2 = types.KeyboardButton('📁 Проверка папок')
    item3 = types.KeyboardButton('❓ Справка')
    item4 = types.KeyboardButton('⬅ Назад')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню настроек', reply_markup=markup)