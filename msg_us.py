from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(token=config.BOT_TOKEN)
bot_logs = Bot(token=config.BOT_TOKEN_logs)


async def answer_message(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if config.author(message.chat.id, config.users):
        await bot_logs.send_message(config.admin_id, text='Пользователь {1} https://t.me/{0}'
                                                          ' ID: `'.format(user_name, first_name) +
                                                          str(message.chat.id) + '`' + " отправил: " + message.text,
                                    parse_mode='Markdown')

        if message.text == "/start":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            await message.answer("Привет, " + message.from_user.first_name +
                                 ", бот создан KnightsOfNarsia. \nСправка /help ", reply_markup=keyboard1)

        elif message.text == "/help":
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
            keyboard.add(types.InlineKeyboardButton('Бесплатные самоцветы',
                                                    url='https://t.me/joinchat/J8dMLy4wRy4yNWIy'))
            await message.answer('Бот создан для облегчения игрового процесса "Битвы Замков".' +
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
                                 '\nЕсли остались вопросы или пожелания, напишите создателю бота.',
                                 reply_markup=keyboard)

        elif message.text.lower() == "нарсия":
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
            await message.answer(text='Выбери интересующую механику:', reply_markup=keyboard)

        elif message.text.lower() == "бг":
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
            await message.answer(text='Выбери интересующую сборку:', reply_markup=keyboard)

        elif message.text.lower() == "локации":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('Смотрители', 'Босс', 'Факела', 'Подземелья', 'Назад')
            await message.answer("Выбери интересующую локацию.", reply_markup=keyboard1)

        elif message.text.lower() == "назад":
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard1.row('ПВП', 'БГ', 'Локации', 'Справки', 'Нарсия')
            await message.answer("Выбери интересующую команду.", reply_markup=keyboard1)

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
            await message.answer(text='Выбери интересующего смотрителя:', reply_markup=keyboard)

        elif message.text.lower() == "подземелья":
            keyboard = types.InlineKeyboardMarkup()
            key_razlom = types.InlineKeyboardButton(text='Разломы/пустоши/саммиты', callback_data='razlom')
            key_more = types.InlineKeyboardButton(text='Море/Меса/Лава', callback_data='more')
            keyboard.add(
                key_razlom,
                key_more
            )
            await message.answer(text='Выбери интересующее подземелье:', reply_markup=keyboard)

        elif message.text.lower() == "босс":
            keyboard = types.InlineKeyboardMarkup()
            key_kremen = types.InlineKeyboardButton(text='Кремень', callback_data='kremen')
            key_parsival = types.InlineKeyboardButton(text='Parsival`', callback_data='parsival')
            keyboard.add(
                key_kremen,
                key_parsival
            )
            await message.answer(text='Выбери одну из двух сборок от  @IKREMEN или @AleksandrHD:',
                                 reply_markup=keyboard)

        elif message.text.lower() == "факела":
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/G80d_E_vTB0'))
            media = types.MediaGroup()
            media.attach_photo(types.InputFile('Database/fakel/bard.jpg'))
            media.attach_photo(types.InputFile('Database/fakel/dino.jpg'))
            media.attach_photo(types.InputFile('Database/fakel/treant.jpg'))
            media.attach_photo(types.InputFile('Database/fakel/chezh.jpg'))
            media.attach_photo(types.InputFile('Database/fakel/okkult.jpg'))
            media.attach_photo(types.InputFile('Database/fakel/mechnick.jpg'))
            await bot.send_media_group(chat_id=message.chat.id, media=media)
            img = open('Database/fakel/pack.png', 'rb')
            await bot.send_photo(chat_id=message.chat.id, photo=img)
            await message.answer("Создатель сборки на факела Сергей @IKREMEN"
                                 "\nБард : реанимация, оживление, крылатое возрождение, священный суд" +
                                 "\nТреант: реанимация, железная воля, крылатое возрождение, священный суд" +
                                 "\nДинамо: пыл битвы, лук порядка/проклятый доспех, крылатое возрождение, амбициозность" +
                                 "\nЧешуекрыл: чаша пожирателя, посох хаоса/проклятый доспех, "
                                 "крылатое возрождение, амбициозность" +
                                 "\nМечник: выживание, воодушевление, крылатое возрождение, священный суд" +
                                 "\nОккультист: крепкая связь, выживание, крылатое возрождение, печать бездны",
                                 reply_markup=keyboard)

        elif message.text.lower() == "справки":
            keyboard = types.InlineKeyboardMarkup()
            key_adapt = types.InlineKeyboardButton(text='Адаптация', callback_data='adapt')
            key_accessory = types.InlineKeyboardButton(text='Экипировка', callback_data='accessory')
            key_dop = types.InlineKeyboardButton(text='Допы', callback_data='dop')
            key_proryv = types.InlineKeyboardButton(text='Прорыв', callback_data='proryv')
            key_pet = types.InlineKeyboardButton(text='Питомцы', callback_data='pet')
            key_setka = types.InlineKeyboardButton(text='Сетка', callback_data='setka')
            key_abbreviation = types.InlineKeyboardButton(text='Аббревиатуры', callback_data='abbreviation')
            key_titul = types.InlineKeyboardButton(text='Титул', callback_data='titul')
            key_dusha = types.InlineKeyboardButton(text='Душа', callback_data='dusha')
            key_suvenir = types.InlineKeyboardButton(text='Сувенир', callback_data='suvenir')
            key_relik = types.InlineKeyboardButton(text='Реликвия', callback_data='relik')
            key_sozv = types.InlineKeyboardButton(text='Созвездия', callback_data='sozv')
            key_gaid_pvp = types.InlineKeyboardButton(text='ПВП', callback_data='gaid_pvp')
            keyboard.add(
                key_titul,
                key_proryv,
                key_dop,
                key_relik,
                key_adapt,
                key_accessory,
                key_suvenir,
                key_dusha,
                key_pet,
                key_setka,
                key_abbreviation,
                key_sozv,
                key_gaid_pvp
            )
            await message.answer(text='Выбери интересующую команду:', reply_markup=keyboard)

        elif message.text.lower() == "пвп":
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
                await message.answer(text='Выбери интересующую сборку героя:', reply_markup=keyboard)
            else:
                bot_logs.send_message(chat_id=config.admin_id, text='Пользователь {1} https://t.me/{0} '
                                                                    'ID: `'.format(user_name, first_name) +
                                                                    str(message.chat.id) + '`' + " без доступа к ПВП",
                                      parse_mode='Markdown')
                await message.answer(
                    text='Для доступа к ПВП пользователь должен находиться в группах Спецназ или Штурмовики.')

    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Создатель бота', url='https://t.me/Vadik3AHO3A'))
        await message.answer('Тебе сюда нельзя. Твой ID: `' + str(message.chat.id) +
                             '`\nОтправьте ID, представленный выше, и игровой Никнейм создателю бота.',
                             parse_mode='Markdown', reply_markup=keyboard)
        bot_logs.send_message(chat_id=config.admin_id, text='Пользователь, у которого нет доступа, {1} https://t.me/{0}'
                                                            ' ID: `'.format(user_name, first_name) +
                                                            str(message.chat.id) + '`' + " отправил: " + message.text,
                              parse_mode='Markdown')