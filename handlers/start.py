import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from const import START_MENU_TEXT
from database import bot_db
from keyboards.start_menu import start_menu_keyboard


async def start_menu(message: types.Message):
    print(message)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    # with open(MEDIA_DESTINATION + "bot.jpg", 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=START_MENU_TEXT.format(
    #             user=message.from_user.first_name
    #         ),
    #         reply_markup=await start_menu_keyboard()
    #     )

    with open(MEDIA_DESTINATION + "bender.gif", 'rb') as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption=START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_menu_keyboard()
        )


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )
