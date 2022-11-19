import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def keyboard_pvp():
    keyboard = telebot.types.InlineKeyboardMarkup()
    list_keyboard = []
    for index, item in enumerate(config.pvp):
        name = config.worksheet_build_pvp.cell(row=int(index) + 2, column=2).value
        key = config.worksheet_build_pvp.cell(row=int(index) + 2, column=1).value
        list_keyboard.append(telebot.types.InlineKeyboardButton(text=name, callback_data=key))
    keyboard.add(*list_keyboard, row_width=3)
    return keyboard


def keyboard_bg():
    keyboard = telebot.types.InlineKeyboardMarkup()
    list_keyboard = []
    for index, item in enumerate(config.bg):
        name = config.worksheet_build_bg.cell(row=int(index) + 2, column=2).value
        key = config.worksheet_build_bg.cell(row=int(index) + 2, column=1).value
        list_keyboard.append(telebot.types.InlineKeyboardButton(text=name, callback_data=key))
    keyboard.add(*list_keyboard, row_width=3)
    keyboard.add(telebot.types.InlineKeyboardButton(text='Мажор-сборка', callback_data='major'))
    return keyboard


def call_pvp(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if config.author(message.chat.id, config.swats):
        keyboard = keyboard_pvp()
        img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
        bot.send_photo(message.chat.id, img, caption='Выбери интересующую сборку героя:',
                       protect_content=True, reply_markup=keyboard)
    else:
        bot_logs.send_message(config.admin_id[0], text='Пользователь {1} @{0} '
                                                    '\nID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + "</code> без доступа к ПВП",
                              parse_mode='HTML')
        bot.send_message(message.chat.id, text='Для доступа к ПВП пользователь должен находиться '
                                                    'в группах Спецназ или Штурмовики.')


def call_bg(message):
    keyboard = keyboard_bg()
    img = 'https://disk.yandex.ru/i/5SMx62WtuDJQOw'
    bot.send_photo(message.chat.id, img, caption='Выбери интересующую сборку героя:',
                   protect_content=True, reply_markup=keyboard)
