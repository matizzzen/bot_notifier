from aiogram import types
from loader import dp
import anek


@dp.message_handler(commands=['start', 'help'])
async def greeting(message: types.Message):
    await message.answer("Привет, теперь будешь уведомленя получать")


@dp.message_handler(commands=['anecdote'])
async def greeting(message: types.Message):
    await message.delete()
    await message.answer(anek.get_anek())


@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await message.answer("я еще маленький бот, не умею грамотно отвечать, но могу /anecdote вкинуть)")
