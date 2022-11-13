import telebot
import config
import location
import narsiya
import table
import build

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def call_user(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if config.author(message.chat.id, config.users):
        if message.chat.id == -1001410785964 or message.chat.id == -1001467336173 or message.chat.id == -1001100054328:
            pass
        else:
            bot_logs.send_message(config.admin_id[0], text='Пользователь {1} @{0}'
                                                    ' ID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + '</code> отправил: ' + message.text,
                              parse_mode='HTML')

        if message.text == "/start" or message.text.lower() == "/start@knightofnarsia_bot":
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +
                             ", бот создан KnightsOfNarsia. \nСправка /help ", reply_markup=keyboard)

        elif message.text == "/help" or message.text.lower() == "/help@knightofnarsia_bot":
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
            keyboard.add(telebot.types.InlineKeyboardButton('Бесплатные самоцветы',
                                                            url='https://t.me/joinchat/J8dMLy4wRy4yNWIy'))
            bot.send_message(message.from_user.id, 'Бот создан для облегчения игрового процесса "Битвы Замков".' +
                             '\nКоманды выведены кнопками на панели.' +
                             '\nСписок команд:' +
                             '\n/start - запуск бота.' +
                             '\n/help - вызов справки.' +
                             '\nПВП - актуальные сборки героев для ПВП режимов.' +
                             '\nБГ - сборки для прохождения Битвы Гильдий.' +
                             '\nЛокации - сборки для прохождения командных подземелий, смотрителя, факела, босса.' +
                             '\nСправки - сводные таблицы, гайды, обозначения.'
                             '\nНарсия - обучение игровому процессу в Нарсии.' +
                             '\nНаш канал по бесплатным самоцветам по ссылке ниже.' +
                             '\nЕсли остались вопросы или пожелания, напишите создателю бота.', reply_markup=keyboard)

        elif message.text.lower() == "нарсия" or message.text.lower() == "/narsiya"\
                or message.text.lower() == "/narsiya@knightofnarsia_bot":
            narsiya.call_narsiya(message)

        elif message.text.lower() == "бг" or message.text.lower() == "/bg"\
                or message.text.lower() == "/bg@knightofnarsia_bot":
            build.call_bg(message)

        elif message.text.lower() == "локации":
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('Смотрители', 'Босс', 'Факела', 'Подземелья', 'Назад')
            bot.send_message(message.chat.id, "Выбери интересующую локацию.", reply_markup=keyboard)

        elif message.text.lower() == "назад":
            keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            bot.send_message(message.chat.id, "Выбери интересующую команду.", reply_markup=keyboard1)

        elif message.text.lower() == "смотрители" or message.text.lower() == "/smotr"\
                or message.text.lower() == "/smotr@knightofnarsia_bot":
            keyboard = telebot.types.InlineKeyboardMarkup()
            key_svyatoy = telebot.types.InlineKeyboardButton(text='Святой', callback_data='svyatoy')
            key_poryadok = telebot.types.InlineKeyboardButton(text='Порядок', callback_data='poryadok')
            key_prorok = telebot.types.InlineKeyboardButton(text='Пророк', callback_data='prorok')
            keyboard.add(
                key_svyatoy,
                key_poryadok,
                key_prorok,
            )
            bot.send_message(message.from_user.id, text='Выбери интересующего смотрителя:', reply_markup=keyboard)

        elif message.text.lower() == "подземелья" or message.text.lower() == "/podzem" \
                or message.text.lower() == "/podzem@knightofnarsia_bot":
            keyboard = keyboard_podzem()
            img = open('Database/bz.jpg', 'rb')
            bot.send_photo(message.chat.id, img, caption='Выбери интересующее подземелье.', reply_markup=keyboard)

        elif message.text.lower() == "босс" or message.text.lower() == "/boss"\
                or message.text.lower() == "/boss@knightofnarsia_bot":
            keyboard = telebot.types.InlineKeyboardMarkup()
            key_kremen = telebot.types.InlineKeyboardButton(text='Кремень', callback_data='kremen')
            key_parsival = telebot.types.InlineKeyboardButton(text='Parsival`', callback_data='parsival')
            keyboard.add(
                key_kremen,
                key_parsival
            )
            bot.send_message(message.from_user.id, text='Выбери одну из двух сборок от  @IKREMEN или @AleksandrHD:',
                             reply_markup=keyboard)

        elif message.text.lower() == "факела" or message.text.lower() == "/fakel"\
                or message.text.lower() == "/fakel@knightofnarsia_bot":
            location.fakel(message.from_user.id)

        elif message.text.lower() == "справки" or message.text.lower() == "/table"\
                or message.text.lower() == "/table@knightofnarsia_bot":
            table.call_table(message)

        elif message.text.lower() == "пвп" or message.text.lower() == "/pvp" \
                or message.text.lower() == "/pvp@knightofnarsia_bot":
            build.call_pvp(message)

    elif message.chat.id == -1001180042310:
        pass

    else:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: <code>' + str(message.chat.id) +
                         '</code>\nОтправьте ID, представленный выше, и игровой Никнейм создателю бота.',
                         parse_mode='HTML', reply_markup=keyboard)
        bot_logs.send_message(config.admin_id[0], text='Пользователь, у которого нет доступа, {1} @{0}'
                                                    ' ID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + "</code> отправил: " + message.text,
                              parse_mode='HTML')

    if "где скюль" in message.text.lower():
        bot.reply_to(message, 'Потеряли пацана')

    elif "скюль" in message.text.lower() and "бот" in message.text.lower():
        bot.reply_to(message, 'Согласен, мой малой')

    elif "скюль ты" in message.text.lower() or "скюль, ты" in message.text.lower():
        bot.reply_to(message, 'По имени и отчеству, пожалуйста')


def keyboard_podzem():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_razlom = telebot.types.InlineKeyboardButton(text='Разлом/пустошь/саммит', callback_data='razlom')
    key_more = telebot.types.InlineKeyboardButton(text='Море/Меса/Лава', callback_data='more')
    keyboard.add(
        key_razlom,
        key_more
    )
    return keyboard
