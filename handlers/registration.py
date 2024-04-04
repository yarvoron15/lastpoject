from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, media
from const import Userinfo
from database import db


class Registration(StatesGroup):
    name = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    gender = State()
    best_color = State()
    photo = State()


async def register_begin(call: types.CallbackQuery):
    datab = db.Database()
    ids = datab.select_id_info(
        tg=call.from_user.id
    )
    if ids:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='U have already registered✅')
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Write ur name'
        )
        await Registration.name.set()


async def load_name(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = m.text
    await bot.send_message(
        chat_id=m.from_user.id,
        text='write ur bio'
    )
    await Registration.next()


async def load_bio(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = m.text

    await bot.send_message(
        chat_id=m.from_user.id,
        text='How old are u?'
    )
    await Registration.next()


async def load_age(m: types.Message, state: FSMContext):
    if m.text.isdigit():
        async with state.proxy() as data:
            data["age"] = m.text
        await bot.send_message(
            chat_id=m.from_user.id,
            text='What is ur zodiac sign?'
        )
        await Registration.next()
    else:
        await bot.send_message(
            chat_id=m.from_user.id,
            text='U should have written only numbers.\n'
                 'U must restart ur registration.'
        )
        await state.finish()


async def load_zodiac(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["zodiac"] = m.text
    await bot.send_message(
        chat_id=m.from_user.id,
        text='What is ur gender?'
    )
    await Registration.next()


async def load_gender(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["gender"] = m.text
    await bot.send_message(
        chat_id=m.from_user.id,
        text='What is ur favorite color?'
    )
    await Registration.next()


async def load_color(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["color"] = m.text
    await bot.send_message(
        chat_id=m.from_user.id,
        text='Send me ur photo\n'
             'it must be default photo.'
    )
    await Registration.next()


async def load_photo(m: types.Message, state: FSMContext):
    path = await m.photo[-1].download(
        destination_dir=media
    )
    datab = db.Database()
    row = datab.select_id_info(
        tg=m.from_user.id
    )

    async with state.proxy() as data:
        datab.insert_info(
            tg=m.from_user.id,
            name=data["name"],
            bio=data["bio"],
            age=data["age"],
            zodiac=data["zodiac"],
            gender=data["gender"],
            color=data["color"],
            photo=path.name
        )
        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=m.from_user.id,
                photo=photo,
                caption=Userinfo.format(
                    name=data['name'],
                    bio=data['bio'],
                    age=data['age'],
                    z=data['zodiac'],
                    gender=data['gender'],
                    bestcolor=data['color']
                )
            )
    await bot.send_message(
        chat_id=m.from_user.id,
        text='U have successfully registered🎉🎊'
    )
    await state.finish()


def register_reg_handler(dp: Dispatcher):
    dp.register_callback_query_handler(register_begin, lambda call: call.data == 'reg')
    dp.register_message_handler(load_name, state=Registration.name, content_types=["text"])
    dp.register_message_handler(load_bio, state=Registration.biography, content_types=["text"])
    dp.register_message_handler(load_age, state=Registration.age, content_types=["text"])
    dp.register_message_handler(load_zodiac, state=Registration.zodiac_sign, content_types=["text"])
    dp.register_message_handler(load_gender, state=Registration.gender, content_types=["text"])
    dp.register_message_handler(load_color, state=Registration.best_color, content_types=["text"])
    dp.register_message_handler(load_photo, state=Registration.photo, content_types=types.ContentTypes.PHOTO)


