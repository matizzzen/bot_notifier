from aiogram import types
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def greeting(message: types.Message):
    await message.answer("Привет, теперь будешь уведомленя получать")


