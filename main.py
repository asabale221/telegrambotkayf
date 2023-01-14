from aiogram import Bot, Dispatcher, types, executor
import config
from random import randrange

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def start(messege: types.Message):
    await messege.answer(f"Здраствуйте {messege.from_user.full_name}Давай сыграем? Я загадал сифру от 1 до 3 угадывай")
    
    n = randrange(1,4)
    n = str(n)

    @dp.message_handler()
    async def echo_message(msg: types.Message):
        mes = msg.text

        if mes == n:
            await bot.send_message(msg.from_user.id, "ООх правильно ты угадал")
        else:
            await bot.send_message(msg.from_user.id, "Давай еше попробуй го го го")

executor.start_polling(dp)