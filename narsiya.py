import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


def call_narsiya(message):
    keyboard = types.InlineKeyboardMarkup()
    key_kamen = types.InlineKeyboardButton(text='Камень', callback_data='kamen')
    key_spam = types.InlineKeyboardButton(text='Спам-пачка', callback_data='spam')
    key_zahvat = types.InlineKeyboardButton(text='Захват', callback_data='zahvat')
    key_othill = types.InlineKeyboardButton(text='Отхил', callback_data='othill')
    key_pos = types.InlineKeyboardButton(text='Атака', callback_data='pos')
    key_deffence = types.InlineKeyboardButton(text='Защита', callback_data='deffence')
    keyboard.add(
        key_kamen,
        key_spam,
        key_zahvat,
        key_othill,
        key_pos,
        key_deffence
    )
    bot.send_message(message.from_user.id, text='Выбери интересующую механику:', reply_markup=keyboard)


def kamen(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/S4Etfs8f5l0'))
    bot.send_message(message,
                     "Для отправки камня в замок гильдии/поселок/город необходимо:"
                     "\n1.Нажать на соответствующий замок гильдии/поселок/город."
                     "\n2.Нажать на кнопку молотка."
                     "\n3.Выбрать количество камня, например, стрелкой вправо максимальное."
                     "\n4.Нажать кнопку подарить.",
                     reply_markup=keyboard
                     )


def spam(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/tyzndFS9CAs'))
    bot.send_message(message,
                     "Создание пачки для спама/захвата клетки:"
                     "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                     "\n2.Нажать на кнопку Создать команду."
                     "\n3.Нажать на кнопку Редактировать."
                     "\n4.Выбрать и поставить на плитки 3х слабых героев."
                     "\n5.Нажать на кнопку сохранить."
                     "\nИспользовать пачку, пока не закончится ХП пачки, далее блок Отхил",
                     reply_markup=keyboard
                     )


def zahvat(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/9VtSfd9wspw'))
    bot.send_message(message,
                     "Для захвата клетки:"
                     "\n1.Нажать на определенную клетку, которую хотите атаковать."
                     "\n2.Нажать на кнопку Меча."
                     "\n3.Выбрать пачку, которой будете атаковать."
                     "\n4.Нажать на кнопку ОК."
                     "\n5.Перед вами откроется окно, где видно время марша, время возвращения, расход воды."
                     "\n6.Нажать на кнопку Высадить.",
                     reply_markup=keyboard
                     )


def othill(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/Zgi10tD15Dk'))
    img = open('Database/othill.png', 'rb')
    bot.send_message(message,
                     "Герои при полном истощении уходят в КД на 10 минут (пример на фото)."
                     "\nДля восстановления ХП героев после истощения:"
                     "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                     "\n2.Нажать на кнопку Создать команду."
                     "\n3.Нажать на кнопку Восстановить силу."
                     "\n4.Нажать у каждого героя +10, чтоб текущая сила героя стала 10/100."
                     "\n5.Нажать на кнопку ОК.",
                     reply_markup=keyboard
                     )
    bot.send_photo(message, img)


def pos(message):
    bot.send_message(message,
                     "Для атаки поселка/города/импа:"
                     "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                     "\n2.Нажать на кнопку Создать команду."
                     "\n3.Нажать на кнопку Редактировать."
                     "\n4.Выбрать и поставить на плитки 3х героев, один из которых 30+ прорыв с полным ХП"
                     "и два слабых героя по 10 ХП."
                     "\n5.Нажать на кнопку сохранить."
                     "\nС каждой атакой восстанавливать ХП у героя с 30+ прорывом и заменять двух слабых героев"
                     "на других по 10 хп."
                     )


def deffence(message):
    bot.send_message(message,
                     "Для защиты поселка/города:"
                     "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                     "\n2.Нажать на кнопку Создать команду."
                     "\n3.Нажать на кнопку Редактировать."
                     "\n4.1.Защита спамом: три слабых героя 10 хп."
                     "\n4.2.Защита фулом: шесть сильнейших героя фул хп."
                     "\n5.Нажать на кнопку сохранить."
                     "\n6.1.Спам менять с каждой атакой врага, не отхилливать фул."
                     "\n6.2.Фул пак: восстанавливать постоянно ХП после атаки врага."
                     )
