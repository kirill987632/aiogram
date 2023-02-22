from aiogram import Bot, Dispatcher, executor, types
from config import token
from cource import convert

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hello I\'m exchange rate bot!\nWrite \'/get_cource\' to start the bot.")

@dp.message_handler(commands=["get_cource"])
async def get_cource(message: types.Message):
    await message.reply(f"Dollar exchange rate now {convert}rub")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)