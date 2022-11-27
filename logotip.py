import telebot
from PIL import Image
import config
import callback
import io

bot = telebot.TeleBot(config.BOT_TOKEN)
bot_logs = telebot.TeleBot(config.BOT_TOKEN_logs)


def create_logo(img):
    x = callback.x
    y = callback.y
    logo = open('Database/logo.png', 'rb')
    background = Image.open(img)
    foreground = Image.open(logo)
    new_image = background.resize((1280, 590))
    new_image.paste(foreground, (x, y), foreground)
    return new_image


def save_photo(message):
    fileid = message.photo[-1].file_id
    file_info = bot.get_file(fileid)
    downloaded_file = bot.download_file(file_info.file_path)
    img = io.BytesIO(downloaded_file)

    user_name = message.from_user.username
    first_name = message.from_user.first_name
    msg_logs = f'Пользователь {first_name} @{user_name}\nID: <code>' + str(message.chat.id) + '</code> отправил.'
    bot_logs.send_photo(config.admin_id[0], img, caption=msg_logs, parse_mode='HTML')
    return img
