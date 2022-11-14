import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


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
