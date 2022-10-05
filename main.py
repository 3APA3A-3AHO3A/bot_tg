"""
cd bot_tg
python main.py
git pull
"""


from aiogram import Bot, Dispatcher, executor, types
import config
import msg_us
import call_us


bot = Bot(token=config.BOT_TOKEN)
bot_logs = Bot(token=config.BOT_TOKEN_logs)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    await msg_us.answer_message(message)


@dp.callback_query_handler()
async def callback_worker(callback: types.CallbackQuery):
    await call_us.answer_callback(callback)


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        pass