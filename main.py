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
import logotip
import send

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['id_file'])
def send_mail(message):
    msg = bot.send_message(message.chat.id, 'Кинь документ.',
                           protect_content=True)
    bot.register_next_step_handler(msg, handle_files)


def handle_files(message):
    document_id = message.document.file_id
    print(document_id)
    # Выводим ссылку на файл
    bot.send_message(message.chat.id, document_id)


@bot.message_handler(content_types=["photo"])
def logo_send(message):
    if config.author(message.chat.id, config.users):
        img = logotip.save_photo(message)
        img_logo = logotip.create_logo(img)
        bot.delete_message(message.chat.id, message.message_id)
        msg = "#castleclash\n" \
              "#cbcevent https://discord.gg/castleclash"
        bot.send_photo(chat_id=message.chat.id, photo=img_logo, caption=msg)


@bot.message_handler(commands=['logo'])
def send_mail(message):
    msg = 'Выберите позицию логотипа.'
    keyboard = creative.keyboard_logo()
    keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки видео', url='https://g.igg.com/EtngH2'))
    keyboard.add(telebot.types.InlineKeyboardButton('Форма для отправки фото', url='https://g.igg.com/oXK3JZ'))
    img = 'https://disk.yandex.ru/i/Qv-USJ8d3vsfww'
    bot.send_photo(message.chat.id, img, caption=msg, reply_markup=keyboard, parse_mode='HTML')
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['donate'])
def donate(message):
    send.donate(message)


@bot.message_handler(commands=['send'])
def send_mail(message):
    if config.author(message.chat.id, config.admin_id):
        msg = bot.send_message(message.chat.id, 'Введите сообщение для рассылки\nДля отмены напишите "-" без кавычек',
                               protect_content=True)
        bot.register_next_step_handler(msg, send.message_mailing)
    else:
        bot.send_message(message.chat.id, 'Нет прав на использование данной команды.', protect_content=True)


@bot.message_handler(commands=['send_bot'])
def send_mail(message):
    if config.author(message.chat.id, config.admin_id):
        msg = bot.send_message(message.chat.id, 'Введите сообщение для рассылки\nДля отмены напишите "-" без кавычек',
                               protect_content=True)
        bot.register_next_step_handler(msg, send.message_mailing_bot)
    else:
        bot.send_message(message.chat.id, 'Нет прав на использование данной команды.', protect_content=True)


@bot.message_handler(content_types=["left_chat_member"])
def handler_left_member(message):
    if message.chat.id == -1001410785964:
        msg = "Боец сдулся. Добро пожаловать в рядовые."
        bot.send_message(message.chat.id, msg, parse_mode='HTML', protect_content=True)
    elif message.chat.id == -1001467336173:
        msg = "Всего хорошего, туалетный воин."
        bot.send_message(message.chat.id, msg, parse_mode='HTML', protect_content=True)


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
