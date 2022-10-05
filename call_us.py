from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(token=config.BOT_TOKEN)

async def answer_callback(callback):
    # ПВП
    strid = str(callback.data)
    for index, item in enumerate(config.pvp):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=6).value) + \
                  "\nСозвездия: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=7).value)
            img = open('Database/sborki/' + str(item) + '.jpg', 'rb')
            await callback.message.answer(msg)
            await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    # БГ
    for index, item in enumerate(config.bg):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=6).value)
            img = open('Database/sborki/bg/' + str(item) + '.jpg', 'rb')
            await callback.message.answer(msg)
            await bot.send_photo(chat_id=callback.from_user.id, photo=img)
    if callback.data == "major":
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/sborki/bg/major/1.jpg'))
        media.attach_photo(types.InputFile('Database/sborki/bg/major/2.jpg'))
        media.attach_photo(types.InputFile('Database/sborki/bg/major/3.jpg'))
        media.attach_photo(types.InputFile('Database/sborki/bg/major/4.jpg'))
        media.attach_photo(types.InputFile('Database/sborki/bg/major/5.jpg'))
        media.attach_photo(types.InputFile('Database/sborki/bg/major/6.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await callback.message.answer("Сборка на БГ от Сергея @IKREMEN")

    # Нарсия
    elif callback.data == "kamen":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/S4Etfs8f5l0'))
        await callback.message.answer("Для отправки камня в замок гильдии/поселок/город необходимо:"
                                      "\n1.Нажать на соответствующий замок гильдии/поселок/город."
                                      "\n2.Нажать на кнопку молотка."
                                      "\n3.Выбрать количество камня, например, стрелкой вправо максимальное."
                                      "\n4.Нажать кнопку подарить.",
                                      reply_markup=keyboard
                                      )

    elif callback.data == "spam":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/tyzndFS9CAs'))
        await callback.message.answer("Создание пачки для спама/захвата клетки:"
                                      "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                                      "\n2.Нажать на кнопку Создать команду."
                                      "\n3.Нажать на кнопку Редактировать."
                                      "\n4.Выбрать и поставить на плитки 3х слабых героев."
                                      "\n5.Нажать на кнопку сохранить."
                                      "\nИспользовать пачку, пока не закончится ХП пачки, далее блок Отхил",
                                      reply_markup=keyboard
                                      )

    elif callback.data == "zahvat":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/9VtSfd9wspw'))
        await callback.message.answer("Для захвата клетки:"
                                      "\n1.Нажать на определенную клетку, которую хотите атаковать."
                                      "\n2.Нажать на кнопку Меча."
                                      "\n3.Выбрать пачку, которой будете атаковать."
                                      "\n4.Нажать на кнопку ОК."
                                      "\n5.Перед вами откроется окно, где видно время марша, время возвращения, расход воды."
                                      "\n6.Нажать на кнопку Высадить.",
                                      reply_markup=keyboard
                                      )

    elif callback.data == "othill":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/Zgi10tD15Dk'))
        img = open('Database/othill.png', 'rb')
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)
        await callback.message.answer("Герои при полном истощении уходят в КД на 10 минут (пример на фото)."
                                      "\nДля восстановления ХП героев после истощения:"
                                      "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                                      "\n2.Нажать на кнопку Создать команду."
                                      "\n3.Нажать на кнопку Восстановить силу."
                                      "\n4.Нажать у каждого героя +10, чтоб текущая сила героя стала 10/100."
                                      "\n5.Нажать на кнопку ОК.",
                                      reply_markup=keyboard
                                      )

    elif callback.data == "pos":
        await callback.message.answer("Для атаки поселка/города/импа:"
                                      "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                                      "\n2.Нажать на кнопку Создать команду."
                                      "\n3.Нажать на кнопку Редактировать."
                                      "\n4.Выбрать и поставить на плитки 3х героев, один из которых 30+ прорыв с полным ХП"
                                      "и два слабых героя по 10 ХП."
                                      "\n5.Нажать на кнопку сохранить."
                                      "\nС каждой атакой восстанавливать ХП у героя с 30+ прорывом и заменять двух слабых героев"
                                      "на других по 10 хп."
                                      )

    elif callback.data == "deffence":
        await callback.message.answer("Для защиты поселка/города:"
                                      "\n1.Нажать справа на одну из трех линий (это ваши пачки)."
                                      "\n2.Нажать на кнопку Создать команду."
                                      "\n3.Нажать на кнопку Редактировать."
                                      "\n4.1.Защита спамом: три слабых героя 10 хп."
                                      "\n4.2.Защита фулом: шесть сильнейших героя фул хп."
                                      "\n5.Нажать на кнопку сохранить."
                                      "\n6.1.Спам менять с каждой атакой врага, не отхилливать фул."
                                      "\n6.2.Фул пак: восстанавливать постоянно ХП после атаки врага."
                                      )

    # Смотрители
    elif callback.data == "svyatoy":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/Geq5h3rP_gM'))
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat1.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat2.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat3.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat4.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat5.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/svyat/svyat6.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await callback.message.answer("Святой:\n" +
                                      "Динамо: Щит дракона, выживание, дрогго\n" +
                                      "Оккультист: Щит дракона, берсерк (8+ уровень), спанчбокс\n" +
                                      "Тесса: Щит дракона, берсерк, крокко\n" +
                                      "Фанатик(Ронин): Щит дракона, берсерк, крокко\n" +
                                      "Спарки: Раскол, проклятый доспех, химерик\n" +
                                      "Сердцеедка: Берсерк, щит дракона, чикабум\n" +
                                      "Техника выпуска тоже важна. Сначала Динамо, после того, как смотритель кинул топор, "
                                      "сразу всех остальных.\n" +
                                      "Важно - никаких пиромагов, иначе проигрыш. Чарой лучше ставить расколенный доспех.\n" +
                                      "***Если Динамо не выживает с щитом порядка (квадрат), пробуйте барьер",
                                      reply_markup=keyboard)

    elif callback.data == "prorok":
        img = open('Database/smotr/prorok/pack.png', 'rb')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok1.png'))
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok2.png'))
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok3.png'))
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok4.png'))
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok5.png'))
        media.attach_photo(types.InputFile('Database/smotr/prorok/prorok6.png'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)
        await callback.message.answer("Пророк (сборка от Сергея @IKREMEN):\n" +
                                      "При высадке важно учитывать, чтобы на первых двух выпущенных героях были питомцы Осьминоги."
                                      "\nСборка на всех героях одна: "
                                      "\nРаскол, Священный огонь, Зелье безумия, Пиромаг."
                                      "\n`На тыкву`: Раскол, Священный огонь, Кровавый барьер, Священный огонь.",
                                      parse_mode='Markdown'
                                      )

    elif callback.data == "poryadok":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/OQ6LBEkHQ3I'))
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok1.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok2.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok3.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok4.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok5.jpg'))
        media.attach_photo(types.InputFile('Database/smotr/poryadok/poryadok6.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await callback.message.answer("Порядок:\n" +
                                      "Голем: Щит дракона, раскол, зелье безумия, Спанчбокс\n" +
                                      "Судья Дэд: Раскол, священный огонь, Кровавый барьер, Раскаленный доспех, Рудольф\n" +
                                      "Мадам Боа: Каменная кожа, Чаша вампира, Кровавый барьер, Иллюзорность\n" +
                                      "Ракшаса: Щит дракона/Каменная кожа, священный огонь, барьер, Сокол\n" +
                                      "Фехтовальщик: Каменная кожа/Щит дракона, священный огонь, барьер, Кицунэ\n" +
                                      "Орфей: Щит дракона/каменная кожа, священный огонь, барьер, Крокко\n" +
                                      "Высадка: первым Голем, за ним остальные под ноги смотрителю. "
                                      "Рудольфа можно заменить на Крокко/Чикабум",
                                      reply_markup=keyboard)

    # Подземелья
    elif callback.data == "razlom":
        img = open('Database/podzem/fault.jpg', 'rb')
        await callback.message.answer("Мадам Боа: раскол, воодушевление, пиромаг. Питомец иллюзорность" +
                                      "\nСтрелок: раскол, священный огонь, Обряд лечения/Пиромаг (питомец любой)" +
                                      "\nХранитель: щит дракона, воодушевление, священный суд/пиромаг" +
                                      "\nВорожей: щит дракона, воодушевление, священный суд" +
                                      "\nПолярный Лис: щит дракона, воодушевление, священный суд" +
                                      "\nФрейя: раскол, воодушевление, пиромаг")
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "more":
        img = open('Database/podzem/sea.jpg', 'rb')
        await callback.message.answer("Бард (любая сборка): каменная кожа, священный огонь, священный суд" +
                                      "\nКнязь Тыква: щит дракона, воодушевление, священный суд" +
                                      "\nСтрелок: раскол, священный огонь, пиромаг/Обряд лечения" +
                                      "\nФрейя: раскол, щит дракона, пиромаг/Обряд лечения" +
                                      "\nМадам Боа: щит дракона, раскол, пиромаг" +
                                      "\nВедьма: щит дракона, раскол, пиромаг")
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "kremen":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/-Hrkj-SAdfk'))
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/boss/kremen/1.jpg'))
        media.attach_photo(types.InputFile('Database/boss/kremen/2.jpg'))
        media.attach_photo(types.InputFile('Database/boss/kremen/3.jpg'))
        media.attach_photo(types.InputFile('Database/boss/kremen/4.jpg'))
        media.attach_photo(types.InputFile('Database/boss/kremen/5.jpg'))
        media.attach_photo(types.InputFile('Database/boss/kremen/6.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await callback.message.answer("Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                                      "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к",
                                      reply_markup=keyboard)

    elif callback.data == "parsival":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/BZLsehTBKlU'))
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/boss/parsival/1.jpg'))
        media.attach_photo(types.InputFile('Database/boss/parsival/2.jpg'))
        media.attach_photo(types.InputFile('Database/boss/parsival/3.jpg'))
        media.attach_photo(types.InputFile('Database/boss/parsival/4.jpg'))
        media.attach_photo(types.InputFile('Database/boss/parsival/5.jpg'))
        media.attach_photo(types.InputFile('Database/boss/parsival/6.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        await callback.message.answer("Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                                      "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к"
                                      "\nДинамо без Пета ставится перед боссом, остальные герои позади босса.",
                                      reply_markup=keyboard)

    # Таблицы
    elif callback.data == "adapt":
        msg = "Таблица адаптаций:"
        img = open('Database/table/adaptation.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)


    elif callback.data == "dusha":
        msg = "Таблица Снаряжения и Души:"
        img = open('Database/table/dusha.png', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "suvenir":
        msg = "Таблица Сувениров:"
        img = open('Database/table/suvenir.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "relik":
        msg = "Таблица Реликвии:"
        img = open('Database/table/relik.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "accessory":
        msg = "Таблица экипировки:"
        await callback.message.answer(msg)
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Database/table/armor.jpg'))
        media.attach_photo(types.InputFile('Database/table/shoes.jpg'))
        media.attach_photo(types.InputFile('Database/table/weapon.jpg'))
        media.attach_photo(types.InputFile('Database/table/helmet.jpg'))
        await bot.send_media_group(chat_id=callback.from_user.id, media=media)

    elif callback.data == "titul":
        msg = "Таблица титула:"
        img = open('Database/table/titul.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "sozv":
        msg = "*Перевод созвездий*:" \
              "\nАтака - Attack" \
              "\nЖизнь - HP" \
              "\nТочность - ACC" \
              "\nУклон - Dodge" \
              "\nКрит удар - CRIT" \
              "\nКрит урон - CRIT DMG" \
              "\nКрит. сопротивление (антикрит) - CRIT Resist"
        await callback.message.answer(msg)

    elif callback.data == "dop":
        msg = "Таблица допов:"
        img = open('Database/table/dops.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "proryv":
        msg = "Таблица прорывов:"
        img = open('Database/table/breakthrough.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "pet":
        msg = "Таблица питомцев:"
        img = open('Database/table/pet.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "setka":
        msg = "Таблица звездной сетки (Смотрителей):"
        img = open('Database/table/grid.jpg', 'rb')
        await callback.message.answer(msg)
        await bot.send_photo(chat_id=callback.from_user.id, photo=img)

    elif callback.data == "abbreviation":
        await callback.message.answer("*Таланты*:" +
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

    elif callback.data == 'gaid_pvp':
        msg = "Гайд от @IKREMEN по ПВП-режимам (Арена, Повелитель Мира, Атака Фортов):" \
              "\n\n1. Высадка героев по линиям:" \
              "\nПервая: три героя, которые собраны на ХП, Сопротивление, понижение урона." \
              "\nВторая: дебаф- и сейв-герои." \
              "\nТретья: дамаг- и рес-герои." \
              "\n\n2. В каждой пачке: Хиллер и дамагер, это и питомцев касается." \
              "\n\n3. В каждой пачке: Один спектр и одно ПВО - обязательно, одна комета - ситуационно." \
              "\n\n4. В каждой пачке: Древнее знание, кошмар, гниль, танец феи и другие топ квадраты." \
              "\n\n5. В каждой пачке: Один из шести героев собран на уклон." \
              "\n\n6. Сборка зависит от прокачки прорыва, реликвии, экипировки."
        await callback.message.answer(msg)