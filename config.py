from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = config('TOKEN')
media = config('MEDIA')
chat_id = config('GROUP')
chat_id1 = config('GROUP1')
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())