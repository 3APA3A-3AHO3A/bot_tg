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
