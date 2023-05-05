from controllers.routes.handlers import allmenu
from model.file_module.create import Create
from model.core.bot import bot
from telebot import types


creation_menu = [
    '✏ Выбрать категорию',
    '✍ Создать категорию',
    '✏ Создать подкатегорию',
    '⬅ Назад'
]

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.chat.type == 'private':
        #####################################
        # Команды, приходящие из данного меню
        #####################################
        if message.text in creation_menu:
            if message.text == creation_menu[0]:
                choose_category(message)
            if message.text == creation_menu[1]:
                create_cat(message)
            if message.text == creation_menu[2]:
                create_sub(message)
            if message.text == creation_menu[3]:
                allmenu.main_menu(message)
        else:
        ######################################
        # Команды, приходящие из главного меню
        ######################################
            if message.text == '✍ Новая категория':
                new_category(message)
            if message.text == '✏ Новая заметка':
                new_note(message)


@bot.message_handler(commands=['note'])
def new_note(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✏ Выбрать категорию')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = Create.create_note()
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['cat'])
def new_category(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✍ Создать категорию')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = Create.create_category()
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['sub'])
def new_subcategory(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✏ Создать подкатегорию')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = Create.create_category()
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['choose_cat'])
def choose_category(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✏ Выбрать данную категорию')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = 'Выбор категории'
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['reate_cat'])
def create_cat(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✏ Введите название для категории')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = 'Создание категории'
    bot.send_message(message.chat.id, answer, reply_markup=markup)


@bot.message_handler(commands=['reate_cat'])
def create_sub(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(u'✏ Введите название для подкатегории')
    item2 = types.KeyboardButton(u'⬅ Назад')
    markup.add(item1, item2)
    answer = 'Создание подкатегории'
    bot.send_message(message.chat.id, answer, reply_markup=markup)