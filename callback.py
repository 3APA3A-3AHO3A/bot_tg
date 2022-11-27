import telebot
import build
import config
import creative
import location
import narsiya
import table

bot = telebot.TeleBot(config.BOT_TOKEN)
x = -40
y = -100


def callback_user(call):
    global x
    global y
    # ПВП
    strid = str(call.data)
    for index, item in enumerate(config.pvp):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=6).value) + \
                  "\nСозвездия: " + str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=7).value)
            img = str(config.worksheet_build_pvp.cell(row=int(index) + 2, column=8).value)
            media = telebot.types.InputMediaPhoto(img, caption=msg)
            bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                   media=media, reply_markup=build.keyboard_pvp())

    # БГ
    for index, item in enumerate(config.bg):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_bg.cell(row=int(index) + 2, column=6).value)
            img = str(config.worksheet_build_bg.cell(row=int(index) + 2, column=7).value)
            media = telebot.types.InputMediaPhoto(img, caption=msg)
            bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                   media=media, reply_markup=build.keyboard_bg())

    if call.data == "major":
        media = [telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/qWGY28C01v5z8w',
                                               caption="Сборка на БГ от Сергея @IKREMEN"),
                 telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/9LlkDIm-2xCpxQ'),
                 telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/BnERAU-ed_Z4qw'),
                 telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/vbDrxbqHW1z_aQ'),
                 telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/q1C1TeqjmGM1XQ'),
                 telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/ys6OSkXjWtivlA')]
        bot.send_media_group(call.message.chat.id, media, protect_content=True)

    # Нарсия
    elif call.data == "kamen":
        narsiya.kamen(call)

    elif call.data == "spam":
        narsiya.spam(call)

    elif call.data == "zahvat":
        narsiya.zahvat(call)

    elif call.data == "othill":
        narsiya.othill(call)

    elif call.data == "pos":
        narsiya.pos(call)

    elif call.data == "deffence":
        narsiya.deffence(call)

    # Смотрители
    elif call.data == "svyatoy":
        location.svyatoy(call)

    elif call.data == "prorok":
        location.prorok(call)

    elif call.data == "poryadok":
        location.poryadok(call)

    # Подземелья
    elif call.data == "razlom":
        location.razlom(call)

    elif call.data == "more":
        location.more(call)

    # Таблицы
    elif call.data == "adapt":
        table.adapt(call)

    elif call.data == "dusha":
        table.dusha(call)

    elif call.data == "suvenir":
        table.suvenir(call)

    elif call.data == "relik":
        table.relik(call)

    elif call.data == "accessory":
        table.ecip(call)

    elif call.data == "titul":
        table.titul(call)

    elif call.data == "sozv":
        table.sozv(call)

    elif call.data == "dop":
        table.dop(call)

    elif call.data == "proryv":
        table.proryv(call)

    elif call.data == "pet":
        table.pet(call)

    elif call.data == "setka":
        table.setka(call)

    elif call.data == "abbreviation":
        table.abbr(call)

    elif call.data == 'gaid_pvp':
        table.gaid_pvp(call)

    elif call.data == "creative_guide":
        creative.creative_guide(call)

    # logo
    elif call.data == 'top_left_position':
        x = -40
        y = -100
        msg = 'Отправьте изображения.'
        keyboard = creative.keyboard_logo()
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
        media = telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/Np7DAJBebYjSEg', caption=msg)
        bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                               media=media, reply_markup=keyboard)

    elif call.data == 'top_right_position':
        x = 900
        y = -100
        msg = 'Отправьте изображения.'
        keyboard = creative.keyboard_logo()
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
        media = telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/NMWY081x0wOCXA', caption=msg)
        bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                               media=media, reply_markup=keyboard)

    elif call.data == 'bottom_left_position':
        x = 0
        y = 300
        msg = 'Отправьте изображения.'
        keyboard = creative.keyboard_logo()
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
        media = telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/XJhqU7i2Fwuh-Q', caption=msg)
        bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                               media=media, reply_markup=keyboard)

    elif call.data == 'bottom_right_position':
        x = 900
        y = 300
        msg = 'Отправьте изображения.'
        keyboard = creative.keyboard_logo()
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
        keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
        media = telebot.types.InputMediaPhoto('https://disk.yandex.ru/i/EPZU-FzL7EjiVQ', caption=msg)
        bot.edit_message_media(message_id=call.message.message_id, chat_id=call.message.chat.id,
                               media=media, reply_markup=keyboard)
