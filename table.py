import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


def call_table(message):
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
    bot.send_message(message.from_user.id, text='Выбери интересующую команду:', reply_markup=keyboard)


def gaid_pvp(message):
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
    bot.send_message(message, msg)

def adapt(message):
    msg = "Таблица адаптаций:"
    img = open('Database/table/adaptation.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def dusha(message):
    msg = "Таблица Снаряжения и Души:"
    img = open('Database/table/dusha.png', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def suvenir(message):
    msg = "Таблица Сувениров:"
    img = open('Database/table/suvenir.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def relik(message):
    msg = "Таблица Реликвии:"
    img = open('Database/table/relik.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def ecip(message):
    bot.send_media_group(message, [types.InputMediaPhoto(open('Database/table/armor.jpg', 'rb'),
                                                         caption="Таблица экипировки."),
                                   types.InputMediaPhoto(open('Database/table/shoes.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/table/weapon.jpg', 'rb')),
                                   types.InputMediaPhoto(open('Database/table/helmet.jpg', 'rb'))])


def titul(message):
    msg = "Таблица титула:"
    img = open('Database/table/titul.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def sozv(message):
    msg = "*Перевод созвездий*:" \
          "\nАтака - Attack" \
          "\nЖизнь - HP" \
          "\nТочность - ACC" \
          "\nУклон - Dodge" \
          "\nКрит удар - CRIT" \
          "\nКрит урон - CRIT DMG" \
          "\nКрит. сопротивление (антикрит) - CRIT Resist"
    bot.send_message(message, msg)


def dop(message):
    msg = "Таблица допов:"
    img = open('Database/table/dops.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def proryv(message):
    msg = "Таблица прорывов:"
    img = open('Database/table/breakthrough.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def pet(message):
    msg = "Таблица питомцев:"
    img = open('Database/table/pet.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def setka(message):
    msg = "Таблица звездной сетки (Смотрителей):"
    img = open('Database/table/grid.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img)


def abbr(message):
    bot.send_message(message, "*Таланты*:" +
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
