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
    key_setka = types.InlineKeyboardButton(text='Звездная сетка', callback_data='setka')
    key_abbreviation = types.InlineKeyboardButton(text='Аббревиатуры', callback_data='abbreviation')
    key_titul = types.InlineKeyboardButton(text='Титул', callback_data='titul')
    key_dusha = types.InlineKeyboardButton(text='Душа', callback_data='dusha')
    key_suvenir = types.InlineKeyboardButton(text='Сувенир', callback_data='suvenir')
    key_relik = types.InlineKeyboardButton(text='Реликвия', callback_data='relik')
    key_sozv = types.InlineKeyboardButton(text='Созвездия', callback_data='sozv')
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
        key_sozv
    )
    bot.send_message(message.from_user.id, text='Выбери интересующие таблицы:', reply_markup=keyboard)


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
    msg = "Таблица экипировки:"
    img1 = open('Database/table/armor.jpg', 'rb')
    img2 = open('Database/table/shoes.jpg', 'rb')
    img3 = open('Database/table/weapon.jpg', 'rb')
    img4 = open('Database/table/helmet.jpg', 'rb')
    bot.send_message(message, msg)
    bot.send_photo(message, img1)
    bot.send_photo(message, img2)
    bot.send_photo(message, img3)
    bot.send_photo(message, img4)


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
