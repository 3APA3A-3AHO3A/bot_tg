import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def logo_mailing(message):
    if message.content_type == "photo":
        user_name = message.from_user.username
        first_name = message.from_user.first_name
        fileid = message.photo[-1].file_id
        file_info = bot.get_file(fileid)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        img = open('image.jpg', 'rb')
        msg = 'Выбери позицию логотипа.'
        keyboard = keyboard_logo()
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
        bot.send_photo(message.chat.id, img, caption=msg, reply_markup=keyboard, parse_mode='HTML')

        msg_logs = f'Пользователь {first_name} @{user_name}\nID: <code>' + str(message.chat.id) + '</code> отправил.'
        bot_logs.send_photo(config.admin_id[0], downloaded_file, caption=msg_logs, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Вызовите заново команду /logo и отправьте фото!')


def keyboard_logo():
    keyboard = telebot.types.InlineKeyboardMarkup()
    top_left_position = telebot.types.InlineKeyboardButton(text='↖', callback_data='top_left_position')
    top_right_position = telebot.types.InlineKeyboardButton(text='↗', callback_data='top_right_position')
    bottom_left_position = telebot.types.InlineKeyboardButton(text='↙', callback_data='bottom_left_position')
    bottom_right_position = telebot.types.InlineKeyboardButton(text='↘', callback_data='bottom_right_position')
    keyboard.add(top_left_position, top_right_position, bottom_left_position, bottom_right_position, row_width=2)
    return keyboard


def keyboard_creative():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
    keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
    return keyboard


def creative(message):
    keyboard = keyboard_creative()
    key_guide = telebot.types.InlineKeyboardButton(text='Инструкция', callback_data='creative_guide')
    keyboard.add(key_guide)
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    msg = 'Выбери команду.\nДля создания лого отправь /logo'
    bot.send_photo(message.chat.id, img, caption=msg, reply_markup=keyboard)


def creative_guide(call):
    msg = 'Гайд по акции "Креативщик":' \
          '\n\nИзображения:' \
          '\n1. Сделайте 6 скриншотов в игре на любую тематику.' \
          '\n2. Добавьте логотип IGG на изображение (можно в нашем боте через команду /logo).' \
          '\n3. Создайте пост на платформе, например VK, Instagram.\n❗ Одно фото - один пост.' \
          '\n4. Добавьте теги в пост (теги указаны ниже).' \
          '\n5. Заполните Google-форму по изображениям.' \
          '\n6. Пример поста по изображениям по ссылке ниже.' \
          '\n\nВидео:' \
          '\n1. Сделайте 6 видеозаписей в игре на любую тематику.' \
          '\n2. Выложите видео на платформе, например VK, YouTube.\n❗ Одно видео - один пост.' \
          '\n3. Добавьте теги в пост (теги указаны ниже).' \
          '\n4. Заполните Google-форму по видеозаписям.' \
          '\n5. Пример поста по видеозаписям по ссылке ниже.' \
          '\n\nТеги:' \
          '\n#castleclash\n' \
          '#cbcevent https://discord.gg/castleclash'
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    keyboard = keyboard_creative()
    keyboard.add(telebot.types.InlineKeyboardButton('Пример видео', url='https://www.youtube.com/watch?v=JFgpF6lJB4Y'))
    keyboard.add(telebot.types.InlineKeyboardButton('Пример изображения', url='https://vk.com/wall246078124_63'))
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard)
