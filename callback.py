import telebot
import config
import location
import narsiya
import table
from telebot import types


bot = telebot.TeleBot(config.BOT_TOKEN)


def callback_user(message, data):
    # ПВП
    strid = str(data)
    for index, item in enumerate(config.pvp):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=6).value) + \
                  "\nСозвездия: " + str(config.worksheet_build_pvp.cell(row=int(index)+2, column=7).value)
            img = open('Database/sborki/'+str(item)+'.jpg', 'rb')
            bot.send_message(message, msg)
            bot.send_photo(message, img)

    # БГ
    for index, item in enumerate(config.bg):
        if str(item) == strid:
            msg = "Герой: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=2).value) + \
                  "\nТалант: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=3).value) + \
                  "\nЭмблема: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=4).value) + \
                  "\nКвадрат: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=5).value) + \
                  "\nЧара: " + str(config.worksheet_build_bg.cell(row=int(index)+2, column=6).value)
            img = open('Database/sborki/bg/'+str(item)+'.jpg', 'rb')
            bot.send_message(message, msg)
            bot.send_photo(message, img)
    if data == "major":
        bot.send_media_group(message, [types.InputMediaPhoto(open('Database/sborki/bg/major/1.jpg', 'rb'),
                                                             caption="Сборка на БГ от Сергея @IKREMEN"),
                                       types.InputMediaPhoto(open('Database/sborki/bg/major/2.jpg', 'rb')),
                                       types.InputMediaPhoto(open('Database/sborki/bg/major/3.jpg', 'rb')),
                                       types.InputMediaPhoto(open('Database/sborki/bg/major/4.jpg', 'rb')),
                                       types.InputMediaPhoto(open('Database/sborki/bg/major/5.jpg', 'rb')),
                                       types.InputMediaPhoto(open('Database/sborki/bg/major/6.jpg', 'rb'))])

    # Нарсия
    elif data == "kamen":
        narsiya.kamen(message)

    elif data == "spam":
        narsiya.spam(message)

    elif data == "zahvat":
        narsiya.zahvat(message)

    elif data == "othill":
        narsiya.othill(message)

    elif data == "pos":
        narsiya.pos(message)

    elif data == "deffence":
        narsiya.deffence(message)

    # Смотрители
    elif data == "svyatoy":
        location.svyatoy(message)

    elif data == "prorok":
        location.prorok(message)

    elif data == "poryadok":
        location.poryadok(message)

    # Подземелья
    elif data == "razlom":
        location.razlom(message)

    elif data == "more":
        location.more(message)

    elif data == "kremen":
        location.boss_kremen(message)

    elif data == "parsival":
        location.boss_persival(message)

    # Таблицы
    elif data == "adapt":
        table.adapt(message)

    elif data == "dusha":
        table.dusha(message)

    elif data == "suvenir":
        table.suvenir(message)

    elif data == "relik":
        table.relik(message)

    elif data == "accessory":
        table.ecip(message)

    elif data == "titul":
        table.titul(message)

    elif data == "sozv":
        table.sozv(message)

    elif data == "dop":
        table.dop(message)

    elif data == "proryv":
        table.proryv(message)

    elif data == "pet":
        table.pet(message)

    elif data == "setka":
        table.setka(message)

    elif data == "abbreviation":
        table.abbr(message)

    elif data == 'gaid_pvp':
        table.gaid_pvp(message)
