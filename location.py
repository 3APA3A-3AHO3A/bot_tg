import telebot
import calling
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


def fakel(chat_id):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Прохождение', url='https://youtu.be/G80d_E_vTB0'))
    keyboard.add(telebot.types.InlineKeyboardButton('Помощник', url='https://youtu.be/MIgKQscYJxo'))
    msg = "Создатель сборки на факела Сергей @IKREMEN" \
          "\nБард : реанимация, оживление, крылатое возрождение, священный суд" \
          "\nТреант: реанимация, железная воля, крылатое возрождение, священный суд" \
          "\nДинамо: пыл битвы, проклятый доспех, крылатое возрождение, амбициозность" \
          "\nЧешуекрыл: чаша пожирателя, посох хаоса/проклятый доспех, крылатое возрождение, амбициозность" \
          "\nМечник: выживание, воодушевление, крылатое возрождение, священный суд" \
          "\nОккультист: крепкая связь, выживание, крылатое возрождение, печать бездны" \
          "\nПо питомцам: обязательно два осьминога, морозный Дракоша, лодка, два луноволка" \
          "\nПосмотрите видео, как добавить помощника по ссылке."
    bot.send_media_group(chat_id, [telebot.types.InputMediaPhoto(open('Database/fakel/pack.png', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/bard.jpg', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/treant.jpg', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/dino.png', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/chezh.jpg', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/okkult.jpg', 'rb')),
                                   telebot.types.InputMediaPhoto(open('Database/fakel/mechnick.jpg', 'rb'))])
    bot.send_message(chat_id, msg, reply_markup=keyboard)


def poryadok(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/OQ6LBEkHQ3I'))
    msg = "Порядок:\n" \
          "Голем: Щит дракона, раскол, зелье безумия, Спанчбокс\n" \
          "Судья Дэд: Раскол, священный огонь, Кровавый барьер, Раскаленный доспех, Рудольф\n" \
          "Мадам Боа: Каменная кожа, Чаша вампира, Кровавый барьер, Иллюзорность\n" \
          "Ракшаса: Щит дракона/Каменная кожа, священный огонь, барьер, Сокол\n" \
          "Фехтовальщик: Каменная кожа/Щит дракона, священный огонь, барьер, Кицунэ\n" \
          "Орфей: Щит дракона/каменная кожа, священный огонь, барьер, Крокко\n" \
          "Высадка: первым Голем, за ним остальные под ноги смотрителю. " \
          "Рудольфа можно заменить на Крокко/Чикабум"
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok1.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok2.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok3.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok4.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok5.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok6.jpg', 'rb'))])
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)


def prorok(call):
    msg = "Пророк (сборка от Сергея @IKREMEN):\n" \
          "При высадке важно учитывать, чтобы на первых двух выпущенных героях были питомцы Осьминоги." \
          "\nСборка на всех героях одна: " \
          "\nРаскол, Священный огонь, Зелье безумия, Пиромаг." \
          "\n<i><b>На тыкву</b></i>: Раскол, Священный огонь, Кровавый барьер, Священный огонь."
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto(open('Database/smotr/prorok/pack.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok1.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok2.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok3.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok4.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok5.png', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/prorok/prorok6.png', 'rb'))])
    bot.send_message(call.message.chat.id, msg, parse_mode='HTML')


def svyatoy(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/Geq5h3rP_gM'))
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat1.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat2.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat3.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat4.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat5.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/smotr/svyat/svyat6.jpg', 'rb'))])
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
                     "***Если Динамо не выживает с щитом порядка (квадрат), пробуйте барьер",
                     reply_markup=keyboard)


def boss_kremen(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/-Hrkj-SAdfk'))
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto(open('Database/boss/kremen/1.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/kremen/2.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/kremen/3.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/kremen/4.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/kremen/5.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/kremen/6.jpg', 'rb'))])
    bot.send_message(call.message.chat.id, "Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                                           "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к",
                     reply_markup=keyboard)


def boss_persival(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/BZLsehTBKlU'))
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto(open('Database/boss/parsival/1.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/parsival/2.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/parsival/3.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/parsival/4.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/parsival/5.jpg', 'rb')),
                          telebot.types.InputMediaPhoto(open('Database/boss/parsival/6.jpg', 'rb'))])
    bot.send_message(call.message.chat.id, "Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                                           "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к"
                                           "\nДинамо без Пета ставится перед боссом, остальные герои позади босса.",
                     reply_markup=keyboard)


def more(call):
    img = open('Database/podzem/sea.jpg', 'rb')
    msg = "Сборка на море/месу/лаву:" \
          "\nБард (любая сборка): каменная кожа, священный огонь, священный суд" \
          "\nКнязь Тыква: щит дракона, воодушевление, священный суд" \
          "\nСтрелок: раскол, священный огонь, пиромаг/Обряд лечения" \
          "\nФрейя: раскол, щит дракона, пиромаг/Обряд лечения" \
          "\nМадам Боа: щит дракона, раскол, пиромаг" \
          "\nВедьма: щит дракона, раскол, пиромаг"
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=calling.keyboard_podzem())


def razlom(call):
    img = open('Database/podzem/fault.jpg', 'rb')
    msg = "Сборка на разлом/пустошь/саммит:" \
          "\nМадам Боа: раскол, воодушевление, пиромаг. Питомец иллюзорность" \
          "\nСтрелок: раскол, священный огонь, Обряд лечения/Пиромаг (питомец любой)" \
          "\nХранитель: щит дракона, воодушевление, священный суд/пиромаг" \
          "\nВорожей: щит дракона, воодушевление, священный суд" \
          "\nПолярный Лис: щит дракона, воодушевление, священный суд" \
          "\nФрейя: раскол, воодушевление, пиромаг"
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=calling.keyboard_podzem())
