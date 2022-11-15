"""
cd bot_tg
python main.py
git pull
"""

import telebot
import config
import callback
import calling
import creative
import send

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['logo'])
def send_mail(message):
    msg = bot.send_message(message.chat.id,
                           'Отправьте изображение боту, на которое нужно наложить логотип')
    bot.register_next_step_handler(msg, creative.logo_mailing)


@bot.message_handler(commands=['donate'])
def donate(message):
    send.donate(message)


@bot.message_handler(commands=['send'])
def send_mail(message):
    if config.author(message.chat.id, config.admin_id):
        msg = bot.send_message(message.chat.id, 'Введите сообщение для рассылки\nДля отмены напишите "-" без кавычек')
        bot.register_next_step_handler(msg, send.message_mailing)
    else:
        bot.send_message(message.chat.id, 'Нет прав на использование данной команды.')


@bot.message_handler(commands=['send_bot'])
def send_mail(message):
    if config.author(message.chat.id, config.admin_id):
        msg = bot.send_message(message.chat.id, 'Введите сообщение для рассылки\nДля отмены напишите "-" без кавычек')
        bot.register_next_step_handler(msg, send.message_mailing_bot)
    else:
        bot.send_message(message.chat.id, 'Нет прав на использование данной команды.')


@bot.message_handler(content_types=["left_chat_member"])
def handler_left_member(message):
    if message.chat.id == -1001410785964:
        msg = "Боец сдулся. Добро пожаловать в рядовые."
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
    elif message.chat.id == -1001467336173:
        msg = "Всего хорошего, туалетный воин."
        bot.send_message(message.chat.id, msg, parse_mode='HTML')


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    send.new_member(message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    calling.call_user(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    callback.callback_user(call)


if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except:
        pass
