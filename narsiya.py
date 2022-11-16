import telebot
import config


bot = telebot.TeleBot(config.BOT_TOKEN)


def keyboard_narsia():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_kamen = telebot.types.InlineKeyboardButton(text='Камень', callback_data='kamen')
    key_spam = telebot.types.InlineKeyboardButton(text='Спам-пачка', callback_data='spam')
    key_zahvat = telebot.types.InlineKeyboardButton(text='Захват', callback_data='zahvat')
    key_othill = telebot.types.InlineKeyboardButton(text='Отхил', callback_data='othill')
    key_pos = telebot.types.InlineKeyboardButton(text='Атака', callback_data='pos')
    key_deffence = telebot.types.InlineKeyboardButton(text='Защита', callback_data='deffence')
    keyboard.add(
        key_kamen,
        key_spam,
        key_zahvat,
        key_othill,
        key_pos,
        key_deffence
    )
    return keyboard


def call_narsiya(message):
    keyboard = keyboard_narsia()
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    bot.send_photo(message.chat.id, img, caption='Выбери интересующую механику:', reply_markup=keyboard)


def kamen(call):
    keyboard = keyboard_narsia()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/S4Etfs8f5l0'))
    msg = "Для отправки камня в замок гильдии/поселок/город необходимо:" \
          "\n1.Нажать на соответствующий замок гильдии/поселок/город." \
          "\n2.Нажать на кнопку молотка." \
          "\n3.Выбрать количество камня, например, стрелкой вправо максимальное." \
          "\n4.Нажать кнопку подарить."
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)


def spam(call):
    keyboard = keyboard_narsia()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/tyzndFS9CAs'))
    msg = "Создание пачки для спама:" \
          "\n1.Нажать справа на одну из трех линий (это ваши пачки)." \
          "\n2.Нажать на кнопку Создать команду." \
          "\n3.Нажать на кнопку Редактировать." \
          "\n4.Выбрать и поставить на плитки 3х слабых героев." \
          "\n5.Нажать на кнопку сохранить." \
          "\nИспользовать пачку, пока не закончится ХП пачки, далее блок Отхил"
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)


def zahvat(call):
    keyboard = keyboard_narsia()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/9VtSfd9wspw'))
    msg = "Для захвата клетки:" \
          "\n1.Нажать на определенную клетку, которую хотите атаковать." \
          "\n2.Нажать на кнопку Меча." \
          "\n3.Выбрать пачку, которой будете атаковать." \
          "\n4.Нажать на кнопку ОК." \
          "\n5.Перед вами откроется окно, где видно время марша, время возвращения, расход воды." \
          "\n6.Нажать на кнопку Высадить."
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)


def othill(call):
    keyboard = keyboard_narsia()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/Zgi10tD15Dk'))
    img = 'https://disk.yandex.ru/i/x0M8jvuNCWilag'
    msg = "Герои при полном истощении уходят в КД на 10 минут (пример на фото)." \
          "\nДля восстановления ХП героев после истощения:" \
          "\n1.Нажать справа на одну из трех линий (это ваши пачки)." \
          "\n2.Нажать на кнопку Создать команду." \
          "\n3.Нажать на кнопку Восстановить силу." \
          "\n4.Нажать у каждого героя +10, чтоб текущая сила героя стала 10/100." \
          "\n5.Нажать на кнопку ОК."
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)


def pos(call):
    keyboard = keyboard_narsia()
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    msg = "Для атаки поселка/города/импа:" \
          "\n1.Нажать справа на одну из трех линий (это ваши пачки)." \
          "\n2.Нажать на кнопку Создать команду." \
          "\n3.Нажать на кнопку Редактировать." \
          "\n4.Выбрать и поставить на плитки 3х героев, один из которых 30+ прорыв с полным ХП" \
          "и два слабых героя по 10 ХП." \
          "\n5.Нажать на кнопку сохранить." \
          "\nС каждой атакой восстанавливать ХП у героя с 30+ прорывом и заменять двух слабых героев" \
          "на других по 10 хп."
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)


def deffence(call):
    keyboard = keyboard_narsia()
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    msg = "Для защиты поселка/города:" \
          "\n1.Нажать справа на одну из трех линий (это ваши пачки)." \
          "\n2.Нажать на кнопку Создать команду." \
          "\n3.Нажать на кнопку Редактировать." \
          "\n4.1.Защита спамом: три слабых героя, один 10 хп, два других 0 хп." \
          "\n4.2.Защита фулом: шесть сильнейших героя фул хп." \
          "\n5.Нажать на кнопку сохранить." \
          "\n6.1.Спам менять с каждой атакой врага, не отхилливать фул героев." \
          "\n6.2.Фул пак: восстанавливать постоянно ХП после атаки врага."
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)
