import telebot
import config
from telebot import types

"""
git init
git add .
git commit -am "update1"
git push heroku master
"""

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def author(chat_id):
    strid = str(chat_id)
    for item in config.users:
        if str(item) == strid:
            return True
    return False


def author_admin(chat_id):
    strid = str(chat_id)
    for item in config.admins:
        if str(item) == strid:
            return True
    return False


def swat(chat_id):
    strid = str(chat_id)
    for item in config.swats:
        if str(item) == strid:
            return True
    return False


@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name

    if author(message.chat.id):
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.row('Пвп', 'Бг', 'Локации', 'Таблицы')
        bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +
                         ", бот создан KnightsOfNarsia. \nСправка /help ", reply_markup=keyboard1)
        bot_logs.send_message(config.admin_id, text='Пользователь, у которого есть доступ, {1} https://t.me/{0}'
        ' запустил бота. ID: ```'.format(user_name, first_name) +
        str(message.chat.id) + '```', parse_mode='Markdown')

    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: ```' + str(message.chat.id) +
                         '```\nОтправьте ID, представленный выше, и игровой Никнейм создателю бота.',
                         parse_mode='Markdown', reply_markup=keyboard)
        bot_logs.send_message(config.admin_id, text='Пользователь, у которого нет доступа, {1} https://t.me/{0}'
                                                    ' запустил бота. ID: ```'.format(user_name, first_name) +
                                                    str(message.chat.id) + '```', parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if author(message.chat.id):
        bot_logs.send_message(config.admin_id, text='Пользователь {1} https://t.me/{0}'
                                                    ' ID: ```'.format(user_name, first_name) +
        str(message.chat.id) + '```' + " отправил: " + message.text, parse_mode='Markdown')
        if message.text == "/help":
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
                             '\nТаблицы - сводные таблицы по игровому процессу.' +
                             '\nНаш канал по бесплатным самоцветам по ссылке ниже.' +
                             '\nЕсли остались вопросы или пожелания, напишите создателю бота.', reply_markup=keyboard)

        elif message.text.title() == "Бг":
            keyboard = types.InlineKeyboardMarkup()
            key_sekach = types.InlineKeyboardButton(text='Секач', callback_data='sekach')
            key_anub = types.InlineKeyboardButton(text='Анубис', callback_data='anub')
            key_bard_bg = types.InlineKeyboardButton(text='Бард', callback_data='bard_bg')
            key_draik = types.InlineKeyboardButton(text='Дрейк', callback_data='draik')
            key_zefir = types.InlineKeyboardButton(text='Зефирик', callback_data='zefir')
            key_minos = types.InlineKeyboardButton(text='Вождь Минотавров', callback_data='minos')
            key_treant = types.InlineKeyboardButton(text='Треант', callback_data='treant')
            key_fen = types.InlineKeyboardButton(text='Феникс', callback_data='fen')
            keyboard.add(
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

        elif message.text.title() == "Локации":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('Смотрители', 'Босс', 'Факела', 'Подземелья', 'Назад')
            bot.send_message(message.chat.id, "Выбери интересующую локацию.", reply_markup=keyboard1)

        elif message.text.title() == "Смотрители":
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

        elif message.text.title() == "Подземелья":
            keyboard = types.InlineKeyboardMarkup()
            key_razlom = types.InlineKeyboardButton(text='Разломы/пустоши/саммиты', callback_data='razlom')
            key_more = types.InlineKeyboardButton(text='Море/Меса/Лава', callback_data='more')
            keyboard.add(
                key_razlom,
                key_more
            )
            bot.send_message(message.from_user.id, text='Выбери интересующее подземелье:', reply_markup=keyboard)

        elif message.text.title() == "Босс":
            keyboard = types.InlineKeyboardMarkup()
            key_boss_16 = types.InlineKeyboardButton(text='16-й уровень', callback_data='boss_16')
            key_boss_any = types.InlineKeyboardButton(text='Любой уровень', callback_data='boss_any')
            keyboard.add(
                key_boss_16,
                key_boss_any
            )
            bot.send_message(message.from_user.id, text='Выбери интересующий уровень босса:', reply_markup=keyboard)

        elif message.text.title() == "Факела":
            keyboard = types.InlineKeyboardMarkup()
            key_fakel = types.InlineKeyboardButton(text='Адский', callback_data='fakel')
            keyboard.add(
                key_fakel
            )
            bot.send_message(message.from_user.id, text='Выбери интересующий уровень факела:', reply_markup=keyboard)

        elif message.text.title() == "Таблицы":
            keyboard = types.InlineKeyboardMarkup()
            key_adapt = types.InlineKeyboardButton(text='Адаптация', callback_data='adapt')
            key_accessory = types.InlineKeyboardButton(text='Экипировка', callback_data='accessory')
            key_dop = types.InlineKeyboardButton(text='Допы', callback_data='dop')
            key_proryv = types.InlineKeyboardButton(text='Прорыв', callback_data='proryv')
            key_pet = types.InlineKeyboardButton(text='Питомцы', callback_data='pet')
            key_setka = types.InlineKeyboardButton(text='Звездная сетка', callback_data='setka')
            key_abbreviation = types.InlineKeyboardButton(text='Аббревиатуры', callback_data='abbreviation')
            key_titul = types.InlineKeyboardButton(text='Титул', callback_data='titul')
            key_dusha = types.InlineKeyboardButton(text='Душа', callback_data='dusha')
            key_relik = types.InlineKeyboardButton(text='Реликвия', callback_data='relik')
            key_sozv = types.InlineKeyboardButton(text='Созвездия', callback_data='sozv')
            keyboard.add(
                key_titul,
                key_proryv,
                key_dop,
                key_relik,
                key_adapt,
                key_accessory,
                key_dusha,
                key_pet,
                key_setka,
                key_abbreviation,
                key_sozv
            )
            bot.send_message(message.from_user.id, text='Выбери интересующие таблицы:', reply_markup=keyboard)
        elif message.text.title() == "Пвп":
            if swat(message.chat.id):
                keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard1.row('Хаос', 'Порядок', 'Назад')
                bot.send_message(message.chat.id, "Выбери смотрителя твоей пачки.", reply_markup=keyboard1)
            else:
                bot_logs.send_message(config.admin_id, text='Пользователь {1} https://t.me/{0} '
                                                            'ID: ```'.format(user_name, first_name) +
                str(message.chat.id) + '```' + " без доступа к ПВП", parse_mode='Markdown')
                bot.send_message(message.from_user.id, text='Для доступа к ПВП пользователь должен находиться'
                                                            'в группах Спецназ или Штурмовики.')
        elif message.text.title() == "Назад":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('Пвп', 'Бг', 'Локации', 'Таблицы')
            bot.send_message(message.chat.id, "Выбери интересующую команду.", reply_markup=keyboard1)
        elif message.text.title() == "Хаос":
            if swat(message.chat.id):
                keyboard = types.InlineKeyboardMarkup()
                key_dinamo = types.InlineKeyboardButton(text='Динамо', callback_data='dinamo')
                key_chezh = types.InlineKeyboardButton(text='Чешуекрыл', callback_data='chezh_chaos')
                key_mechnic = types.InlineKeyboardButton(text='Мечник', callback_data='mechnic')
                key_demon = types.InlineKeyboardButton(text='Демон-охотник', callback_data='demon')
                key_bard = types.InlineKeyboardButton(text='Бард', callback_data='bard')
                key_hudozhka = types.InlineKeyboardButton(text='Художница', callback_data='hudozhka')
                key_mumiya = types.InlineKeyboardButton(text='Мумия', callback_data='mumiya')
                key_mari = types.InlineKeyboardButton(text='Мэри', callback_data='mari')
                key_tycva = types.InlineKeyboardButton(text='Тыква', callback_data='tycva')

                keyboard.add(
                    key_dinamo,
                    key_chezh,
                    key_mechnic,
                    key_demon,
                    key_bard,
                    key_hudozhka,
                    key_mumiya,
                    key_mari,
                    key_tycva
                )
                bot.send_message(message.from_user.id, text='Выбери интересующую сборку героя:',
                                 reply_markup=keyboard)

        elif message.text.title() == "Порядок":
            if swat(message.chat.id):
                keyboard = types.InlineKeyboardMarkup()
                key_dinamo = types.InlineKeyboardButton(text='Динамо', callback_data='dinamo')
                key_chezh = types.InlineKeyboardButton(text='Чешуекрыл', callback_data='chezh_poryadok')
                key_mechnic = types.InlineKeyboardButton(text='Мечник', callback_data='mechnic')
                key_frostee = types.InlineKeyboardButton(text='Фрости', callback_data='frostee')
                key_bard = types.InlineKeyboardButton(text='Бард', callback_data='bard')
                key_mari = types.InlineKeyboardButton(text='Мэри', callback_data='mari')
                key_tycva = types.InlineKeyboardButton(text='Тыква', callback_data='tycva')
                key_maestro = types.InlineKeyboardButton(text='Маэстро', callback_data='maestro')
                key_krist = types.InlineKeyboardButton(text='Кристелла', callback_data='krist')
                key_fairy = types.InlineKeyboardButton(text='Фейри', callback_data='fairy')
                key_okkult = types.InlineKeyboardButton(text='Оккультист', callback_data='okkult')
                key_koloss = types.InlineKeyboardButton(text='Колосс', callback_data='koloss')

                keyboard.add(
                    key_dinamo,
                    key_chezh,
                    key_mechnic,
                    key_frostee,
                    key_bard,
                    key_mari,
                    key_tycva,
                    key_maestro,
                    key_krist,
                    key_fairy,
                    key_okkult,
                    key_koloss
                )
                bot.send_message(message.from_user.id, text='Выбери интересующую сборку героя:',
                                 reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
        bot.send_message(message.chat.id, 'Тебе сюда нельзя. Твой ID: ```' + str(message.chat.id) +
                         '```\nОтправьте ID, представленный выше, и игровой Никнейм создателю бота.',
                         parse_mode='Markdown', reply_markup=keyboard)
        bot_logs.send_message(config.admin_id, text='Пользователь, у которого нет доступа, {1} https://t.me/{0}'
                                                    ' ID: ```'.format(user_name, first_name) +
        str(message.chat.id) + '```' + " отправил: " + message.text, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # ПВП
    strid = str(call.data)
    for index, item in enumerate(config.pvp):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=6).value) + \
                  "\nСозвездия: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=7).value)
            img = open('Database/sborki/'+str(item)+'.jpg', 'rb')
            bot.send_message(call.message.chat.id, msg)
            bot.send_photo(call.message.chat.id, img)

    # БГ
    for index, item in enumerate(config.bg):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=6).value)
            img = open('Database/sborki/bg/'+str(item)+'.jpg', 'rb')
            bot.send_message(call.message.chat.id, msg)
            bot.send_photo(call.message.chat.id, img)


    if call.data == "svyatoy":
        img1 = open('Database/smotr/svyat/svyat1.jpg', 'rb')
        img2 = open('Database/smotr/svyat/svyat2.jpg', 'rb')
        img3 = open('Database/smotr/svyat/svyat3.jpg', 'rb')
        img4 = open('Database/smotr/svyat/svyat4.jpg', 'rb')
        img5 = open('Database/smotr/svyat/svyat5.jpg', 'rb')
        img6 = open('Database/smotr/svyat/svyat6.jpg', 'rb')
        video = open('Database/smotr/svyat/svyat.mp4', 'rb')
        bot.send_message(call.message.chat.id,
                         "Святой:\n" +
                         "Динамо: Щит дракона, выживание, дрогго\n" +
                         "Оккультист: Щит дракона, берсерк (8+ уровень), спанчбокс\n" +
                         "Тесса: Щит дракона, берсерк, крокко\n" +
                         "Фанатик(Ронин): Щит дракона, берсерк, крокко\n" +
                         "Спарки: Раскол, проклятый доспех, химерик\n" +
                         "Сердцеедка: Берсерк, щит дракона, чикабум\n" +
                         "Техника выпуска тоже важна. Сначала Динамо, после того, как смотритель кинул топор, "
                         "сразу всех остальных.\n" +
                         "Важно - никаких пиромагов, иначе проигрыш. Чарой лучше ставить расколенный доспех.\n" +
                         "***Если Динамо не выживает с щитом порядка (квадрат), пробуйте барьер"
                         )
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)
        bot.send_video(call.message.chat.id, video)

    elif call.data == "prorok":
        img1 = open('Database/smotr/prorok/prorok1.jpg', 'rb')
        img2 = open('Database/smotr/prorok/prorok2.jpg', 'rb')
        img3 = open('Database/smotr/prorok/prorok3.jpg', 'rb')
        img4 = open('Database/smotr/prorok/prorok4.jpg', 'rb')
        img5 = open('Database/smotr/prorok/prorok5.jpg', 'rb')
        img6 = open('Database/smotr/prorok/prorok6.jpg', 'rb')
        bot.send_message(call.message.chat.id,
                         "Пророк:\n" +
                         "Динамо: Бастион, раскол, тирания\n" +
                         "Художница: Священный огонь, выживание, управление временем\n" +
                         "Спарки: Священный огонь, выживание, кровавый барьер\n" +
                         "Мадам Боа: Священный огонь, выживание, тирания\n" +
                         "Жрица Воды: Стойкость, выживание, щит порядка\n" +
                         "Князь Тыква: Священный огонь, исцеление, сказочный круг\n"
                         )
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)

    elif call.data == "poryadok":
        img1 = open('Database/smotr/poryadok/poryadok1.jpg', 'rb')
        img2 = open('Database/smotr/poryadok/poryadok2.jpg', 'rb')
        img3 = open('Database/smotr/poryadok/poryadok3.jpg', 'rb')
        img4 = open('Database/smotr/poryadok/poryadok4.jpg', 'rb')
        img5 = open('Database/smotr/poryadok/poryadok5.jpg', 'rb')
        img6 = open('Database/smotr/poryadok/poryadok6.jpg', 'rb')
        video = open('Database/smotr/poryadok/poryadok.mp4', 'rb')
        bot.send_message(call.message.chat.id,
                         "Порядок:\n" +
                         "Голем: Щит дракона, раскол, зелье безумия, Спанчбокс\n" +
                         "Судья Дэд: Раскол, священный огонь, Кровавый барьер, Раскаленный доспех, Рудольф\n" +
                         "Мадам Боа: Каменная кожа, Чаша вампира, Кровавый барьер, Иллюзорность\n" +
                         "Ракшаса: Щит дракона/Каменная кожа, священный огонь, барьер, Сокол\n" +
                         "Фехтовальщик: Каменная кожа/Щит дракона, священный огонь, барьер, Кицунэ\n" +
                         "Орфей: Щит дракона/каменная кожа, священный огонь, барьер, Крокко\n" +
                         "Высадка: первым Голем, за ним остальные под ноги смотрителю. "
                         "Рудольфа можно заменить на Крокко/Чикабум"
                         )
        # bot.send_photo(call.message.chat.id, img1, img2, img3, img4, img5, img6)
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)
        bot.send_video(call.message.chat.id, video)

    elif call.data == "razlom":
        img = open('Database/podzem/fault.jpg', 'rb')
        bot.send_message(call.message.chat.id, "Мадам Боа: раскол, воодушевление, пиромаг. Питомец иллюзорность" +
                         "\nСтрелок: раскол, священный огонь, Обряд лечения/Пиромаг (питомец любой)" +
                         "\nХранитель: щит дракона, воодушевление, священный суд/пиромаг" +
                         "\nВорожей: щит дракона, воодушевление, священный суд" +
                         "\nПолярный Лис: щит дракона, воодушевление, священный суд" +
                         "\nФрейя: раскол, воодушевление, пиромаг")
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "more":
        img = open('Database/podzem/sea.jpg', 'rb')
        bot.send_message(call.message.chat.id, "Бард (любая сборка): каменная кожа, священный огонь, священный суд" +
                         "\nКнязь Тыква: щит дракона, воодушевление, священный суд" +
                         "\nСтрелок: раскол, священный огонь, пиромаг/Обряд лечения" +
                         "\nФрейя: раскол, щит дракона, пиромаг/Обряд лечения" +
                         "\nМадам Боа: щит дракона, раскол, пиромаг" +
                         "\nВедьма: щит дракона, раскол, пиромаг")
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "boss_16":
        img = open('Database/boss/pack.jpg', 'rb')
        img1 = open('Database/boss/bard.jpg', 'rb')
        img2 = open('Database/boss/tycva.jpg', 'rb')
        img3 = open('Database/boss/okkult.jpg', 'rb')
        img4 = open('Database/boss/afina.jpg', 'rb')
        img5 = open('Database/boss/sparki.jpg', 'rb')
        img6 = open('Database/boss/vor.jpg', 'rb')
        bot.send_message(call.message.chat.id, "Бард (любая сборка): священный огонь, воодушевление, священный суд" +
                         "\nКнязь Тыква: щит дракона, раскол, зелье безумия, священный суд" +
                         "\nСпарки: раскол, комета, вдохновение, ураган" +
                         "\nВорожей: раскол, щит дракона/каменная кожа, броня хаоса, священный суд" +
                         "\nОккультист: берсерк, священный огонь, кровавый барьер, священный суд" +
                         "\nАфина: берсерк, священный огонь, крылатое возрождение, священный суд"+
                         "\nСборки могут отличаться, экспериментируйте")
        bot.send_photo(call.message.chat.id, img)
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)

    elif call.data == "boss_any":
        img = open('Database/boss/any/pack.jpg', 'rb')
        img1 = open('Database/boss/any/orf.jpg', 'rb')
        img2 = open('Database/boss/any/tycva.jpg', 'rb')
        img3 = open('Database/boss/any/sparki.jpg', 'rb')
        img4 = open('Database/boss/any/dad.jpg', 'rb')
        img5 = open('Database/boss/any/hudozh.jpg', 'rb')
        img6 = open('Database/boss/any/boa.jpg', 'rb')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/m4gGNVuGUNs'))
        bot.send_message(call.message.chat.id, "Питомцы на героях должны быть именно такими:"
                                               "\nТыква - сокол (м)"
                                               "\nСпарки - кицунэ (м)"
                                               "\nСудья Дэд - ангелок"
                                               "\nХудожница - король осьминог (м)"
                                               "\nОрфей - ледышка"
                                               "\nМадам Боа - резвая летучая мышь",
                         reply_markup=keyboard)
        bot.send_photo(call.message.chat.id, img)
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)

    elif call.data == "fakel":
        img = open('Database/fakel/pack.jpg', 'rb')
        img1 = open('Database/fakel/bard.jpg', 'rb')
        img2 = open('Database/fakel/treant.jpg', 'rb')
        img3 = open('Database/fakel/dino.jpg', 'rb')
        img4 = open('Database/fakel/chezh.jpg', 'rb')
        img5 = open('Database/fakel/fairy.jpg', 'rb')
        img6 = open('Database/fakel/mechnick.jpg', 'rb')
        video = open('Database/fakel/fakel.mp4', 'rb')
        bot.send_message(call.message.chat.id, "Бард : реанимация, оживление, крылатое возрождение, священный суд" +
                         "\nТреант: реанимация, железная воля, крылатое возрождение, священный суд" +
                         "\nДинамо: пыл битвы, лук порядка/проклятый доспех, крылатое возрождение, амбициозность" +
                         "\nЧешуекрыл: чаша пожирателя, посох хаоса/проклятый доспех, крылатое возрождение, амбициозность" +
                         "\nМечник: выживание, воодушевление, крылатое возрождение, священный суд" +
                         "\nФейри: реанимация, выживание, крылатое возрождение, священный суд"
                         )
        bot.send_photo(call.message.chat.id, img)
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)
        bot.send_photo(call.message.chat.id, img5)
        bot.send_photo(call.message.chat.id, img6)
        bot.send_video(call.message.chat.id, video)

    elif call.data == "adapt":
        msg = "Таблица адаптаций:"
        img = open('Database/table/adaptation.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "dusha":
        msg = "Таблица Снаряжения и Души:"
        img = open('Database/table/dusha.png', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "relik":
        msg = "Таблица Реликвии:"
        img = open('Database/table/relik.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "accessory":
        msg = "Таблица экипировки:"
        img1 = open('Database/table/armor.jpg', 'rb')
        img2 = open('Database/table/shoes.jpg', 'rb')
        img3 = open('Database/table/weapon.jpg', 'rb')
        img4 = open('Database/table/helmet.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img1)
        bot.send_photo(call.message.chat.id, img2)
        bot.send_photo(call.message.chat.id, img3)
        bot.send_photo(call.message.chat.id, img4)

    elif call.data == "titul":
        msg = "Таблица титула:"
        img = open('Database/table/titul.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "sozv":
        msg = "Перевод созвездий:" \
              "\nАтака - Attack" \
              "\nЖизнь - HP" \
              "\nТочность - ACC" \
              "\nУклон - Dodge" \
              "\nКрит удар - CRIT" \
              "\nКрит урон - CRIT DMG" \
              "\nКрит. сопротивление (антикрит) - CRIT Resist"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "dop":
        msg = "Таблица допов:"
        img = open('Database/table/dops.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "proryv":
        msg = "Таблица прорывов:"
        img = open('Database/table/breakthrough.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "pet":
        msg = "Таблица питомцев:"
        img1 = open('Database/table/pet.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img1)

    elif call.data == "setka":
        msg = "Таблица звездной сетки (Смотрителей):"
        img = open('Database/table/grid.jpg', 'rb')
        bot.send_message(call.message.chat.id, msg)
        bot.send_photo(call.message.chat.id, img)

    elif call.data == "abbreviation":
        bot.send_message(call.message.chat.id, "*Таланты*:" +
                         "\nОЗ - огненная защита" +
                         "\nСО - священный огонь" +
                         "\nПП - порочный пакт" +
                         "\nИВ - истинная вера" +
                         "\nЩД - щит дракона" +
                         "\nЦД - целитель душ" +
                         "\nПД - проклятый доспех" +
                         "\nОЖ - огонь жизни" +
                         "\nДЖ - дар жизни" +
                         "\nГС - грубая сила" +
                         "\nТУ - тихое укрытие" +
                         "\nКК - каменная кожа" +
                         "\nВода (водушка) - воодушевление" +
                         "\nВж - выживание" +
                         "\n\n*Чары*:" +
                         "\nСС (суд) - священный суд" +
                         "\nПенек - обряд лечения" +
                         "\nРД - раскаленный доспех" +
                         "\n\n*Квадраты*:" +
                         "\nЩП - щит порядка" +
                         "\nБХ - броня хаоса" +
                         "\nКрылья - крылатое возрождение" +
                         "\nКБ - кровавый барьер" +
                         "\nШип - шипастый щит" +
                         "\n\n*Созвездия*:" +
                         "\nТочка - точность" +
                         "\nАнтикрит - критическое сопротивления" +
                         "\nКрит/Удар - критический удар" +
                         "\nАТК - атака", parse_mode='Markdown')


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        pass