import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


def keyboard_table():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_adapt = telebot.types.InlineKeyboardButton(text='Адаптация', callback_data='adapt')
    key_accessory = telebot.types.InlineKeyboardButton(text='Экипировка', callback_data='accessory')
    key_dop = telebot.types.InlineKeyboardButton(text='Допы', callback_data='dop')
    key_proryv = telebot.types.InlineKeyboardButton(text='Прорыв', callback_data='proryv')
    key_pet = telebot.types.InlineKeyboardButton(text='Питомцы', callback_data='pet')
    key_setka = telebot.types.InlineKeyboardButton(text='Сетка', callback_data='setka')
    key_abbreviation = telebot.types.InlineKeyboardButton(text='Аббревиатуры', callback_data='abbreviation')
    key_titul = telebot.types.InlineKeyboardButton(text='Титул', callback_data='titul')
    key_dusha = telebot.types.InlineKeyboardButton(text='Душа', callback_data='dusha')
    key_suvenir = telebot.types.InlineKeyboardButton(text='Сувенир', callback_data='suvenir')
    key_relik = telebot.types.InlineKeyboardButton(text='Реликвия', callback_data='relik')
    key_sozv = telebot.types.InlineKeyboardButton(text='Созвездия', callback_data='sozv')
    key_gaid_pvp = telebot.types.InlineKeyboardButton(text='ПВП', callback_data='gaid_pvp')
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
    return keyboard


def call_table(message):
    keyboard = keyboard_table()
    img = open('Database/bz.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Выбери интересующую команду:', reply_markup=keyboard)


def gaid_pvp(call):
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
    img = open('Database/bz.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def adapt(call):
    msg = "Таблица адаптаций:"
    img = open('Database/table/adaptation.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def dusha(call):
    msg = "Таблица Снаряжения и Души:"
    img = open('Database/table/dusha.png', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def suvenir(call):
    msg = "Таблица Сувениров:"
    img = open('Database/table/suvenir.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def relik(call):
    msg = "Таблица Реликвии:"
    img = open('Database/table/relik.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def ecip(call):
    bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('Database/table/armor.jpg', 'rb'),
                                                                              caption="Таблица экипировки."),
                                                telebot.types.InputMediaPhoto(open('Database/table/shoes.jpg', 'rb')),
                                                telebot.types.InputMediaPhoto(open('Database/table/weapon.jpg', 'rb')),
                                                telebot.types.InputMediaPhoto(open('Database/table/helmet.jpg', 'rb'))])


def titul(call):
    msg = "Таблица титула:"
    img = open('Database/table/titul.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def sozv(call):
    msg = "<b>Перевод созвездий</b>:" \
          "\nАтака - Attack" \
          "\nЖизнь - HP" \
          "\nТочность - ACC" \
          "\nУклон - Dodge" \
          "\nКрит удар - CRIT" \
          "\nКрит урон - CRIT DMG" \
          "\nКрит. сопротивление (антикрит) - CRIT Resist"
    img = open('Database/bz.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg, parse_mode='HTML')
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def dop(call):
    msg = "Таблица допов:"
    img = open('Database/table/dops.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def proryv(call):
    bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('Database/table/proryv.jpg', 'rb'),
                                                                              caption="Таблица прорывов."),
                                                telebot.types.InputMediaPhoto(
                                                    open('Database/table/proryv2.jpg', 'rb'))])


def pet(call):
    msg = "Таблица питомцев:"
    img = open('Database/table/pet.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def setka(call):
    msg = "Таблица звездной сетки (Смотрителей):"
    img = open('Database/table/grid.jpg', 'rb')
    media = telebot.types.InputMediaPhoto(img, caption=msg)
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())


def abbr(call):
    img = open('Database/bz.jpg', 'rb')
    msg = "<b>Таланты</b>:" \
          "\nОЗ - огненная защита" \
          "\nСО - священный огонь" \
          "\nПП - порочный пакт" \
          "\nИВ - истинная вера" \
          "\nЩД - щит дракона" \
          "\nЦД - целитель душ" \
          "\nПД - проклятый доспех" \
          "\nОЖ - огонь жизни" \
          "\nДЖ - дар жизни" \
          "\nГС - грубая сила" \
          "\nТУ - тихое укрытие" \
          "\nКК - каменная кожа" \
          "\nВода (водушка) - воодушевление" \
          "\nВж - выживание" \
          "\n\n<b>Чары</b>:" \
          "\nСС (суд) - священный суд" \
          "\nПенек - обряд лечения" \
          "\nРД - раскаленный доспех" \
          "\n\n<b>Квадраты</b>:" \
          "\nЩП - щит порядка" \
          "\nБХ - броня хаоса" \
          "\nКрылья - крылатое возрождение" \
          "\nКБ - кровавый барьер" \
          "\nШип - шипастый щит" \
          "\n\n<b>Созвездия</b>:" \
          "\nТочка - точность" \
          "\nАнтикрит - критическое сопротивления" \
          "\nКрит/Удар - критический удар" \
          "\nАТК - атака"
    media = telebot.types.InputMediaPhoto(img, caption=msg, parse_mode='HTML')
    bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                           media=media, reply_markup=keyboard_table())
