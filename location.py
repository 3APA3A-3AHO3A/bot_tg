import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.BOT_TOKEN)

def fakel(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/G80d_E_vTB0'))
    msg = "Создатель сборки на факела Сергей @IKREMEN" \
          "\nБард : реанимация, оживление, крылатое возрождение, священный суд" \
          "\nТреант: реанимация, железная воля, крылатое возрождение, священный суд" \
          "\nДинамо: пыл битвы, лук порядка/проклятый доспех, крылатое возрождение, амбициозность" \
          "\nЧешуекрыл: чаша пожирателя, посох хаоса/проклятый доспех, крылатое возрождение, амбициозность" \
          "\nМечник: выживание, воодушевление, крылатое возрождение, священный суд" \
          "\nОккультист: крепкая связь, выживание, крылатое возрождение, печать бездны"
    img = open('Database/fakel/pack.png', 'rb')
    bot.send_photo(message, img)
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/fakel/bard.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/fakel/treant.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/fakel/dino.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/fakel/chezh.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/fakel/okkult.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/fakel/mechnick.jpg', 'rb'))])
    bot.send_message(message, msg, reply_markup=keyboard)

def poryadok(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/OQ6LBEkHQ3I'))
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok1.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok2.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok3.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok4.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok5.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/poryadok/poryadok6.jpg', 'rb'))])
    bot.send_message(message,
                     "Порядок:\n" +
                     "Голем: Щит дракона, раскол, зелье безумия, Спанчбокс\n" +
                     "Судья Дэд: Раскол, священный огонь, Кровавый барьер, Раскаленный доспех, Рудольф\n" +
                     "Мадам Боа: Каменная кожа, Чаша вампира, Кровавый барьер, Иллюзорность\n" +
                     "Ракшаса: Щит дракона/Каменная кожа, священный огонь, барьер, Сокол\n" +
                     "Фехтовальщик: Каменная кожа/Щит дракона, священный огонь, барьер, Кицунэ\n" +
                     "Орфей: Щит дракона/каменная кожа, священный огонь, барьер, Крокко\n" +
                     "Высадка: первым Голем, за ним остальные под ноги смотрителю. "
                     "Рудольфа можно заменить на Крокко/Чикабум",
                     reply_markup=keyboard)

def prorok(message):
    img = open('Database/smotr/prorok/pack.png', 'rb')
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/smotr/prorok/prorok1.png', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/prorok/prorok2.png', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/prorok/prorok3.png', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/prorok/prorok4.png', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/prorok/prorok5.png', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/prorok/prorok6.png', 'rb'))])
    bot.send_photo(message, img)
    bot.send_message(message,
                     "Пророк (сборка от Сергея @IKREMEN):\n" +
                     "При высадке важно учитывать, чтобы на первых двух выпущенных героях были питомцы Осьминоги."
                     "\nСборка на всех героях одна: "
                     "\nРаскол, Священный огонь, Зелье безумия, Пиромаг."
                     "\n<i><b>На тыкву</b></i>: Раскол, Священный огонь, Кровавый барьер, Священный огонь.",
                     parse_mode='HTML'
                     )

def svyatoy(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео', url='https://youtu.be/Geq5h3rP_gM'))
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/smotr/svyat/svyat1.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/svyat/svyat2.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/svyat/svyat3.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/svyat/svyat4.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/svyat/svyat5.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/smotr/svyat/svyat6.jpg', 'rb'))])
    bot.send_message(message,
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

def boss_kremen(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/-Hrkj-SAdfk'))
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/boss/kremen/1.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/kremen/2.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/kremen/3.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/kremen/4.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/kremen/5.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/kremen/6.jpg', 'rb'))])
    bot.send_message(message, "Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                              "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к",
                     reply_markup=keyboard)

def boss_persival(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Видео-прохождение', url='https://youtu.be/BZLsehTBKlU'))
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/boss/parsival/1.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/parsival/2.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/parsival/3.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/parsival/4.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/parsival/5.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/boss/parsival/6.jpg', 'rb'))])
    bot.send_message(message, "Важно! Никаких пиромагов, тамплиеров, мастеров клинка чарами"
                              "\nПитомцев на героях ставить так, чтоб на героях точность была около 20к"
                              "\nДинамо без Пета ставится перед боссом, остальные герои позади босса.",
                     reply_markup=keyboard)

def more(message):
    img = open('Database/podzem/sea.jpg', 'rb')
    bot.send_message(message, "Бард (любая сборка): каменная кожа, священный огонь, священный суд" +
                     "\nКнязь Тыква: щит дракона, воодушевление, священный суд" +
                     "\nСтрелок: раскол, священный огонь, пиромаг/Обряд лечения" +
                     "\nФрейя: раскол, щит дракона, пиромаг/Обряд лечения" +
                     "\nМадам Боа: щит дракона, раскол, пиромаг" +
                     "\nВедьма: щит дракона, раскол, пиромаг")
    bot.send_photo(message, img)

def razlom(message):
    img = open('Database/podzem/fault.jpg', 'rb')
    bot.send_message(message, "Мадам Боа: раскол, воодушевление, пиромаг. Питомец иллюзорность" +
                     "\nСтрелок: раскол, священный огонь, Обряд лечения/Пиромаг (питомец любой)" +
                     "\nХранитель: щит дракона, воодушевление, священный суд/пиромаг" +
                     "\nВорожей: щит дракона, воодушевление, священный суд" +
                     "\nПолярный Лис: щит дракона, воодушевление, священный суд" +
                     "\nФрейя: раскол, воодушевление, пиромаг")
    bot.send_photo(message, img)
