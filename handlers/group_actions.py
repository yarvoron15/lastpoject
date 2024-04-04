from aiogram import types, Dispatcher
from config import bot, chat_id, chat_id1
from database import db
from profanity_check import predict_prob


async def group_filter_message(m: types.Message):
    print(m.chat.id)
    datab = db.Database()
    bad_word = predict_prob([m.text])
    if bad_word > 0.7:
        datab.insert_ban(tg_id=m.from_user.id, first_name=m.from_user.first_name)
        datab.update_count_bun_table(tg_id=m.from_user.id)
        count = datab.select_count_bun_table(tg_id=m.from_user.id)
        count = count[0]
        await m.delete()
        if count < 3:
            await bot.send_message(
                chat_id=m.chat.id,
                text=f'user: {m.from_user.first_name}\n'
                     f'U have written bad word\n'
                     f'It was {count}th time\n'
                     f'If u do it 3rd time\n'
                     f'U will be banned!!'

            )
        else:
            datab.delete_user(tg_id=m.from_user.id)
            await bot.send_message(
                chat_id=m.chat.id,
                text=f'user: {m.from_user.first_name}\n'
                     f'U wrote bad word 3rd time '
                     f'I must ban u!'

            )

            await bot.ban_chat_member(
                chat_id=m.chat.id,
                user_id=m.from_user.id
            )


def register_group_filter(dp: Dispatcher):
    dp.register_message_handler(group_filter_message, lambda m: m.chat.id in [int(chat_id1), int(chat_id)])