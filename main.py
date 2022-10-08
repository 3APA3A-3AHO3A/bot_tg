"""
cd bot_tg
python main.py
git pull
"""

import telebot
import config
import callback
import calling

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['send'])
def send_mail(message):
    if message.chat.id == config.admin_id:
        msg = bot.send_message(message.chat.id, 'Введите текст для рассылки')
        bot.register_next_step_handler(msg, message_mailing)
    else:
        bot.send_message(message.chat.id, 'Нет прав на использование данной команды.')


def message_mailing(message):
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    text = message.text
    if message.text.startswith('-'):
        bot.send_message(message.chat.id, text="Рассылка отменена")
    else:
        bot.send_message(message.chat.id, text='Рассылка начата!')
        for i in config.users:
            bot.send_message(i, text="Сообщение от @{0}\n\n".format(user_name)+str(text))
        bot.send_message(message.chat.id, text=' Рассылка завершена!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    calling.call_user(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    callback.callback_user(call.message.chat.id, call.data)


if __name__ == '__main__':
    try:
        bot.infinity_polling()
        # bot.polling(none_stop=True)
    except:
        pass
