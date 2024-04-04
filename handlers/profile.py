import sqlite3
from random import choice

from aiogram import types, Dispatcher

from config import bot
from const import Userinfo
from database import db
from buttons import inlinebuttons


async def view_random_profile(call: types.CallbackQuery):
    data = db.Database()
    prof = data.select_all_registr(tg_id=call.from_user.id)
    if prof:
        rand = choice(prof)[:9]
        with open(rand[-1], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=Userinfo.format(
                    name=rand[2],
                    bio=rand[3],
                    age=rand[4],
                    z=rand[5],
                    gender=rand[6],
                    bestcolor=rand[7]
                ),
                reply_markup=await inlinebuttons.like_dislike(rand[1])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id, text='Nobody left'
        )


async def like_dislike_management(call: types.CallbackQuery):
    data = db.Database()
    calldata = call.data.split("_")
    try:
        data.insert_like_dislike_table(
            user=calldata[1],
            liker=call.from_user.id,
            what=calldata[0]
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have already valued this profile"
        )
    finally:
        await call.message.delete()
        await view_random_profile(call=call)


def registr_edit_profile(dp: Dispatcher):
    dp.register_callback_query_handler(view_random_profile, lambda call: call.data == 'view')
    dp.register_callback_query_handler(like_dislike_management, lambda call: 'Like' in call.data)
    dp.register_callback_query_handler(like_dislike_management, lambda call: 'Dis' in call.data)