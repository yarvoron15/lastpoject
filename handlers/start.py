from aiogram import types, Dispatcher
from config import bot
from aiogram.utils.deep_linking import _create_link
import sqlite3
from database import db
from buttons import inlinebuttons


async def start(m: types.Message):
    data = db.Database()
    command = m.get_full_command()[1]
    if command != '':
        link = await _create_link('start', payload=command)
        owner = data.select_all_from_tl_users_by_link(link=link)[1]
        ids = data.select_tg_id_user_table(tg_id=m.from_user.id)
        if owner != m.from_user.id:
            if ids is None:
                try:
                    data.insert_referral_table(owner=owner, referral=m.from_user.id)
                    data.update_tg_user_balance(tg_id=owner)
                except sqlite3.IntegrityError:
                    pass
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='U can not use ur own link'
            )
            return
        data.insert_user(
            tg_user_id=m.from_user.id,
            tg_username=m.from_user.first_name
        )
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'hello {m.from_user.first_name}\n',
            reply_markup=await inlinebuttons.quest_button()

        )
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text=f'hello {m.from_user.first_name}\n',
            reply_markup=await inlinebuttons.quest_button()

        )
        data.insert_user(
            tg_user_id=m.from_user.id,
            tg_username=m.from_user.first_name
        )


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')