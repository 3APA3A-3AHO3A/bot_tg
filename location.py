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
    bot.send_media_group(chat_id, [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/vIZaGM3A9pbQHw'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Ic1jbd8I3sDkzw'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/R2yVH8kaZp7xbA'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/bRhK8ukEPEiVnQ'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/qqnWSUgVtYa7wQ'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/L-w94K5Y6-ZpsQ'),
                                   telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/tmIrRnY2fmZ_Dw')],
                         protect_content=True)
    bot.send_message(chat_id, msg, reply_markup=keyboard, protect_content=True)


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
                         [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/hHlEzKcSsvYudA'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/ZG736ShlhWYt1w'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/G3o12M3-_2OSGQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Eqz3pUw7fXmmJQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/A_vf7_fkHkdlFQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/09mbxExEk-JL9w')],
                         protect_content=True)
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard, protect_content=True)


def prorok(call):
    msg = "Пророк (сборка от Сергея @IKREMEN):\n" \
          "При высадке важно учитывать, чтобы на первых двух выпущенных героях были питомцы Осьминоги." \
          "\nСборка на всех героях одна: " \
          "\nРаскол, Священный огонь, Зелье безумия, Пиромаг." \
          "\n<i><b>На тыкву</b></i>: Раскол, Священный огонь, Кровавый барьер, Священный огонь."
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/v_OF6rZC03oneQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/fWDOwvm85Bm2mg'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/wbdCYW1xvIh5Tw'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/bqkK2-r7EuchsA'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Zo55KycRR1jySg'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Twf1J4If02CoTA'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Wu67iB4hFNnhFg')],
                         protect_content=True)
    bot.send_message(call.message.chat.id, msg, parse_mode='HTML', protect_content=True)


def svyatoy(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео', url='https://youtu.be/Geq5h3rP_gM'))
    bot.send_media_group(call.message.chat.id,
                         [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/SezHrYB7L0ewFA'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/ULMvahr5TVgZMQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/2iJCGveHSaGhow'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/I3ARgLx_fNvI9g'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/ANUxp2vyFdh8XQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/W71F-fHLj-jPyA')],
                         protect_content=True)
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
                     reply_markup=keyboard, protect_content=True)


def boss(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/wJnQrLUcUZ8'))
    bot.send_media_group(message.chat.id,
                         [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/o1atSjLlcOeAOQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/OddX_kbNCJEQnw'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/_4YhRNLMmFlXwg'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/gcjrk_H-w6aW9w'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/WvJczu6fH5fNZQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/iLIlW7WGzK73eQ'),
                          telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/J7n-1ZZyOQ70jw')],
                         protect_content=True)
    bot.send_message(message.chat.id, "Важно!\n❗Не ставить чарой: пиромагов, тамплиеров, мастеров клинка."
                                      "\n❗Ставить на героев питомцев, которые не атакуют и дают точность около 20к."
                                      "\n❗Динамо без Пета ставится перед боссом, остальные герои позади него.",
                     reply_markup=keyboard, protect_content=True)


def more(call):
    img = 'https://disk.yandex.ru/i/H2OcA5rg-5UrdA'
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
    img = 'https://disk.yandex.ru/i/JdULohj1BnTjTg'
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
