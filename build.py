import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def keyboard_pvp():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_dinamo = telebot.types.InlineKeyboardButton(text='Динамо', callback_data='dinamo')
    key_chezh_poryadok = telebot.types.InlineKeyboardButton(text='Чех (Порядок)',
                                                            callback_data='chezh_poryadok')
    key_chezh_chaos = telebot.types.InlineKeyboardButton(text='Чех (Хаос)', callback_data='chezh_chaos')
    key_zmeya = telebot.types.InlineKeyboardButton(text='Змей', callback_data='zmeya')
    key_baron = telebot.types.InlineKeyboardButton(text='Барон', callback_data='baron')
    key_povelitel = telebot.types.InlineKeyboardButton(text='Повелитель', callback_data='povelitel')
    key_mechnic = telebot.types.InlineKeyboardButton(text='Мечник', callback_data='mechnic')
    key_bard = telebot.types.InlineKeyboardButton(text='Бард', callback_data='bard')
    key_hudozhka = telebot.types.InlineKeyboardButton(text='Художница', callback_data='hudozhka')
    key_mari = telebot.types.InlineKeyboardButton(text='Мэри', callback_data='mari')
    key_fox = telebot.types.InlineKeyboardButton(text='Лис', callback_data='fox')
    key_frostee = telebot.types.InlineKeyboardButton(text='Фрости', callback_data='frostee')
    key_fairy = telebot.types.InlineKeyboardButton(text='Фейри', callback_data='fairy')
    key_okkult = telebot.types.InlineKeyboardButton(text='Оккультист', callback_data='okkult')
    key_ronin = telebot.types.InlineKeyboardButton(text='Ронин', callback_data='ronin')
    keyboard.add(
        key_zmeya,
        key_dinamo,
        key_chezh_poryadok,
        key_chezh_chaos,
        key_mechnic,
        key_fairy,
        key_bard,
        key_baron,
        key_frostee,
        key_povelitel,
        key_okkult,
        key_hudozhka,
        key_mari,
        key_ronin,
        key_fox,
        row_width=3
    )
    return keyboard


def keyboard_bg():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_sekach = telebot.types.InlineKeyboardButton(text='Секач', callback_data='sekach')
    key_anub = telebot.types.InlineKeyboardButton(text='Анубис', callback_data='anub')
    key_bard_bg = telebot.types.InlineKeyboardButton(text='Бард', callback_data='bard_bg')
    key_draik = telebot.types.InlineKeyboardButton(text='Дрейк', callback_data='draik')
    key_zefir = telebot.types.InlineKeyboardButton(text='Зефирик', callback_data='zefir')
    key_minos = telebot.types.InlineKeyboardButton(text='Вождь Минотавров', callback_data='minos')
    key_treant = telebot.types.InlineKeyboardButton(text='Треант', callback_data='treant')
    key_fen = telebot.types.InlineKeyboardButton(text='Феникс', callback_data='fen')
    key_major = telebot.types.InlineKeyboardButton(text='Мажор-сборка', callback_data='major')
    keyboard.add(
        key_sekach,
        key_anub,
        key_bard_bg,
        key_draik,
        key_zefir,
        key_minos,
        key_treant,
        key_fen,
        row_width=3
    )
    keyboard.add(key_major)
    return keyboard


def call_pvp(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if config.author(message.chat.id, config.swats):
        keyboard = keyboard_pvp()
        img = open('Database/bz.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption='Выбери интересующую сборку героя:', reply_markup=keyboard)
    else:
        bot_logs.send_message(config.admin_id[0], text='Пользователь {1} @{0} '
                                                    '\nID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + "</code> без доступа к ПВП",
                              parse_mode='HTML')
        bot.send_message(message.from_user.id, text='Для доступа к ПВП пользователь должен находиться '
                                                    'в группах Спецназ или Штурмовики.')


def call_bg(message):
    keyboard = keyboard_bg()
    img = open('Database/bz.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Выбери интересующую сборку героя:', reply_markup=keyboard)
