import cfg
from loader import bot, storage
from aiogram import executor
from handlers import dp
import asyncio
from datetime import datetime


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


async def scheduled():
    while True:
        now = datetime.now().strftime("%H:%M")
        print(now)

        if now in cfg.time1:
            for user in cfg.user:
                await bot.send_message(user, f"пилюля")

        if now in cfg.time2:
            for user in cfg.user:
                await bot.send_message(user, f"таблетка")
        await asyncio.sleep(60)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled())
    executor.start_polling(dp, on_shutdown=on_shutdown, skip_updates=True)
