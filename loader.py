from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import cfg

bot = Bot(token=cfg.token, parse_mode=types.ParseMode.HTML, proxy='http://proxy.server:3128')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
