import telebot
import config
from telebot import types
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
        bot_logs.send_message(config.admin_id, text='Пользователь {1} @{0}'
                                                    ' ID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + '</code> отправил: ' + message.text,
                              parse_mode='HTML')

        if message.text == "/start":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +
                             ", бот создан KnightsOfNarsia. \nСправка /help ", reply_markup=keyboard1)

        elif message.text == "/help":
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
            keyboard.add(types.InlineKeyboardButton('Бесплатные самоцветы',
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

        elif message.text.lower() == "нарсия":
            narsiya.call_narsiya(message)

        elif message.text.lower() == "бг":
            build.call_bg(message)

        elif message.text.lower() == "локации":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('Смотрители', 'Босс', 'Факела', 'Подземелья', 'Назад')
            bot.send_message(message.chat.id, "Выбери интересующую локацию.", reply_markup=keyboard1)

        elif message.text.lower() == "назад":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            bot.send_message(message.chat.id, "Выбери интересующую команду.", reply_markup=keyboard1)

        elif message.text.lower() == "смотрители":
            keyboard = types.InlineKeyboardMarkup()
            key_svyatoy = types.InlineKeyboardButton(text='Святой', callback_data='svyatoy')
            key_poryadok = types.InlineKeyboardButton(text='Порядок', callback_data='poryadok')
            key_prorok = types.InlineKeyboardButton(text='Пророк', callback_data='prorok')
            keyboard.add(
                key_svyatoy,
                key_poryadok,
                key_prorok,
            )
            bot.send_message(message.from_user.id, text='Выбери интересующего смотрителя:', reply_markup=keyboard)

        elif message.text.lower() == "подземелья":
            keyboard = types.InlineKeyboardMarkup()
            key_razlom = types.InlineKeyboardButton(text='Разломы/пустоши/саммиты', callback_data='razlom')
            key_more = types.InlineKeyboardButton(text='Море/Меса/Лава', callback_data='more')
            keyboard.add(
                key_razlom,
                key_more
            )
            bot.send_message(message.from_user.id, text='Выбери интересующее подземелье:', reply_markup=keyboard)

        elif message.text.lower() == "босс":
            keyboard = types.InlineKeyboardMarkup()
            key_kremen = types.InlineKeyboardButton(text='Кремень', callback_data='kremen')
            key_parsival = types.InlineKeyboardButton(text='Parsival`', callback_data='parsival')
            keyboard.add(
                key_kremen,
                key_parsival
            )
            bot.send_message(message.from_user.id, text='Выбери одну из двух сборок от  @IKREMEN или @AleksandrHD:',
                             reply_markup=keyboard)

        elif message.text.lower() == "факела":
            location.fakel(message.from_user.id)

        elif message.text.lower() == "справки":
            table.call_table(message)

        elif message.text.lower() == "пвп":
            build.call_pvp(message)

    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: <code>' + str(message.chat.id) +
                         '</code>\nОтправьте ID, представленный выше, и игровой Никнейм создателю бота.',
                         parse_mode='HTML', reply_markup=keyboard)
        bot_logs.send_message(config.admin_id, text='Пользователь, у которого нет доступа, {1} @{0}'
                                                    ' ID: <code>'.format(user_name, first_name) +
                                                    str(message.chat.id) + "</code> отправил: " + message.text,
                              parse_mode='HTML')
