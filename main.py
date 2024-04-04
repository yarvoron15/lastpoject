from config import dp
from aiogram import executor, Dispatcher
from database import db
from handlers import start,questions,group,registration,profile,reference,scrap


async def on_startup(_):
    data = db.Database()
    data.creat_table()


start.register_start(dp=dp)
questions.register_ask(dp=dp)
registration.register_reg_handler(dp=dp)
profile.registr_edit_profile(dp=dp)
reference.register_referrence(dp=dp)
scrap.register_scrap(dp=dp)
group.register_group_filter(dp=dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)