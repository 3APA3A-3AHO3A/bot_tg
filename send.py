import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def message_mailing(message):
    if message.content_type == "text":
        user_name = message.from_user.username
        text = message.text
        if "-" in message.text:
            bot.send_message(message.chat.id, text="Рассылка отменена")
        else:
            bot.send_message(message.chat.id, text='Рассылка начата!')
            for i in config.users:
                try:
                    bot.send_message(i, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
                except:
                    pass
            try:
                bot.send_message(-1001180042310, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
                bot.send_message(-1001100054328, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
                bot.send_message(-1001410785964, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
                bot.send_message(-1001467336173, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
            except:
                pass
            bot.send_message(message.chat.id, text=' Рассылка завершена!')
    elif message.content_type == "photo" or message.content_type == "video":
        bot.send_message(message.chat.id, text='Рассылка начата!')
        for i in config.users:
            try:
                bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.id)
            except:
                pass
        try:
            bot.copy_message(chat_id=-1001180042310, from_chat_id=message.chat.id, message_id=message.id)
            bot.copy_message(chat_id=-1001100054328, from_chat_id=message.chat.id, message_id=message.id)
            bot.copy_message(chat_id=-1001410785964, from_chat_id=message.chat.id, message_id=message.id)
            bot.copy_message(chat_id=-1001467336173, from_chat_id=message.chat.id, message_id=message.id)
        except:
            pass
        bot.send_message(message.chat.id, text=' Рассылка завершена!')


def message_mailing_bot(message):
    if message.content_type == "text":
        user_name = message.from_user.username
        text = message.text
        if "-" in message.text:
            bot.send_message(message.chat.id, text="Рассылка отменена")
        else:
            bot.send_message(message.chat.id, text='Рассылка начата!')
            for i in config.users:
                try:
                    bot.send_message(i, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
                except:
                    pass
            try:
                bot.send_message(-1001467336173, text="Сообщение от @{0}\n\n".format(user_name) + str(text))
            except:
                pass
            bot.send_message(message.chat.id, text=' Рассылка завершена!')
    elif message.content_type == "photo" or message.content_type == "video":
        bot.send_message(message.chat.id, text='Рассылка начата!')
        for i in config.users:
            try:
                bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.id)
            except:
                pass
        try:
            bot.copy_message(chat_id=-1001467336173, from_chat_id=message.chat.id, message_id=message.id)
        except:
            pass
        bot.send_message(message.chat.id, text=' Рассылка завершена!')


def new_member(message):
    # Общалка
    if message.chat.id == -1001467336173:
        first_name = message.new_chat_members[0].first_name
        user_name = message.new_chat_members[0].username
        msg = f"Добро пожаловать в Гильдию <b>KnightsOfNarsia</b>, {first_name} @{user_name} 🤝" \
              "\n\n<b>Основные правила</b>:" \
              "\nЗапрещены мат, политика, оскорбления, провокации, скрины с других проектов." \
              "\nПервый раз - предупреждение, второй - кик." \
              "\n\nПриоритетным направлением развития для KnightsOfNarsia является участие в " \
              "<b>PVP-событиях</b>, что требует от Вас развития аккаунта в правильном русле, т.е. " \
              "<b>АКТУАЛЬНЫЕ</b> сборки, которые можно уточнить в чате, " \
              "для героев под определенные события. " \
              "В Гильдии присутствуют компетентные и опытные игроки, которые обозначат Вам " \
              "вектор и приоритет развития конкретно для Вашего алтаря." \
              "\n\n❗Локация <b>Нарсия</b> является приоритетным событием, регистрация и актив " \
              "в котором <b>ОБЯЗАТЕЛЬНЫ</b>. Имеет смысл сразу же узнать подробности о режиме и " \
              "разобраться в нём, чтобы в будущем не было проблем." \
              "\n\nЖдем Ваших вопросов и, прежде всего, активной игры🗡🛡"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
    # Штурмовики
    elif message.chat.id == -1001410785964:
        first_name = message.new_chat_members[0].first_name
        user_name = message.new_chat_members[0].username
        msg = f"Добро пожаловать в Штурмовики, {first_name} @{user_name} 🤝" \
              "\n\n🗡<b>Штурмовая группа</b>🛡" \
              "\nЭто ступень между рядовым, новеньким бойцом, которого мы ещё не видели " \
              "в Нарсии, и матерым воином нашего 🗡<b>Рыцарского Спецназа🛡</b>" \
              "\n\n<b>Подробнее</b> о Штурмовой группе:" \
              "\nДанная группа является активной группой в Нарсии, которая кует Наш результат и успех, " \
              "Наши победы. Задачи различны: от захвата ресурсов и прокладки дорог до затяжных боев, " \
              "включающих атаку и деф. Также все сборы, забеги, бои до последней капли ресурсов." \
              "\n\nРазвитие в группе и Гильдии зависит только от Вас. Хотите ли Вы развиваться, расти и " \
              "добиваться успехов в PVP или нет. В данной группе Вас ожидают опытные наставники, " \
              "воюющие на ТОП-уровне; интересные и важные задачи в Нарсии, от выполнения которых зависит " \
              "Наш реальный результат." \
              "\nДобро пожаловать в команду👍"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
    # Спецназ
    elif message.chat.id == -1001100054328:
        first_name = message.new_chat_members[0].first_name
        user_name = message.new_chat_members[0].username
        msg = f"Добро пожаловать в <b>Спецназ</b>, {first_name} @{user_name} 🤝" \
              "\n\nТеперь Ты не являешься сопливым бойцом и Сам можешь быть наставником новичкам🗡🛡"
        bot.send_message(message.chat.id, msg, parse_mode='HTML')


def donate(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('donate', url='https://yoomoney.ru/to/410012184021666/0'))
    img = open('Database/donate.jpg', 'rb')
    msg = 'Если Вы хотите поддержать разработчика бота, то можете отправить средства на:' \
          '\n\n<b>Тинькофф</b>:' \
          '\nНомер телефона: <code>+79087057188</code>' \
          '\nНомер карты: <code>2200700464227569</code>' \
          '\n\n<b>Сбербанк</b>:' \
          '\nНомер телефона: <code>+79823214514</code>' \
          '\nНомер карты: <code>5469720013411935</code>' \
          '\n\nОтсканируйте QR-code камерой телефона или перейдите по ссылке.'
    bot.send_photo(message.chat.id, img, caption=msg, reply_markup=keyboard, parse_mode='HTML')
    bot_logs.send_message(config.admin_id[0], text=f'Пользователь {first_name} @{user_name} открыл пожертвование.')
