from aiogram import types
from loader import dp
import anek


@dp.message_handler(commands=['start', 'help'])
async def greeting(message: types.Message):
    await message.answer("Привет, теперь будешь уведомленя получать, но я еще маленький бот, не умею говорить, но я передам твои слова создателю, надеюсь они не злые")


@dp.message_handler(commands=['anecdote'])
async def anec(message: types.Message):
    await message.answer(anek.get_anek())


@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await message.answer("угу, передам")
    with open('log.txt', 'r') as original:
        data = original.read()
    with open('log.txt', 'w') as modified:
        modified.write(f'{data}\n {message.date.time()} {message.from_user.username}: {message.text} ')
