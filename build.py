from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def call_pvp(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if config.author(message.chat.id, config.swats):
        keyboard = types.InlineKeyboardMarkup()
        key_dinamo = types.InlineKeyboardButton(text='Динамо', callback_data='dinamo')
        key_chezh_poryadok = types.InlineKeyboardButton(text='Чех(Порядок)',
                                                        callback_data='chezh_poryadok')
        key_chezh_chaos = types.InlineKeyboardButton(text='Чех(Хаос)', callback_data='chezh_chaos')
        key_zmeya = types.InlineKeyboardButton(text='Змей', callback_data='zmeya')
        key_baron = types.InlineKeyboardButton(text='Барон', callback_data='baron')
        key_povelitel = types.InlineKeyboardButton(text='Повелитель', callback_data='povelitel')
        key_mechnic = types.InlineKeyboardButton(text='Мечник', callback_data='mechnic')
        key_demon = types.InlineKeyboardButton(text='Демон-охотник', callback_data='demon')
        key_bard = types.InlineKeyboardButton(text='Бард', callback_data='bard')
        key_hudozhka = types.InlineKeyboardButton(text='Художница', callback_data='hudozhka')
        key_mumiya = types.InlineKeyboardButton(text='Мумия', callback_data='mumiya')
        key_mari = types.InlineKeyboardButton(text='Мэри', callback_data='mari')
        key_fox = types.InlineKeyboardButton(text='Лис', callback_data='fox')
        key_tycva = types.InlineKeyboardButton(text='Тыква', callback_data='tycva')
        key_frostee = types.InlineKeyboardButton(text='Фрости', callback_data='frostee')
        key_maestro = types.InlineKeyboardButton(text='Маэстро', callback_data='maestro')
        key_krist = types.InlineKeyboardButton(text='Кристелла', callback_data='krist')
        key_fairy = types.InlineKeyboardButton(text='Фейри', callback_data='fairy')
        key_okkult = types.InlineKeyboardButton(text='Оккультист', callback_data='okkult')
        key_koloss = types.InlineKeyboardButton(text='Колосс', callback_data='koloss')
        key_ronin = types.InlineKeyboardButton(text='Ронин', callback_data='ronin')
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
            key_maestro,
            key_krist,
            key_demon,
            key_mumiya,
            key_tycva,
            key_koloss
        )
        bot.send_message(message.from_user.id, text='Выбери интересующую сборку героя:',
                         reply_markup=keyboard)
    else:
        bot_logs.send_message(config.admin_id, text='Пользователь {1} https://t.me/{0} '
                                                    'ID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + "<code> без доступа к ПВП",
                              parse_mode='HTML')
        bot.send_message(message.from_user.id, text='Для доступа к ПВП пользователь должен находиться '
                                                    'в группах Спецназ или Штурмовики.')


def call_bg(message):
    keyboard = types.InlineKeyboardMarkup()
    key_sekach = types.InlineKeyboardButton(text='Секач', callback_data='sekach')
    key_anub = types.InlineKeyboardButton(text='Анубис', callback_data='anub')
    key_bard_bg = types.InlineKeyboardButton(text='Бард', callback_data='bard_bg')
    key_draik = types.InlineKeyboardButton(text='Дрейк', callback_data='draik')
    key_zefir = types.InlineKeyboardButton(text='Зефирик', callback_data='zefir')
    key_minos = types.InlineKeyboardButton(text='Вождь Минотавров', callback_data='minos')
    key_treant = types.InlineKeyboardButton(text='Треант', callback_data='treant')
    key_fen = types.InlineKeyboardButton(text='Феникс', callback_data='fen')
    key_major = types.InlineKeyboardButton(text='Мажор-сборка', callback_data='major')
    keyboard.add(
        key_major,
        key_sekach,
        key_anub,
        key_bard_bg,
        key_draik,
        key_zefir,
        key_minos,
        key_treant,
        key_fen
    )
    bot.send_message(message.from_user.id, text='Выбери интересующую сборку:', reply_markup=keyboard)
