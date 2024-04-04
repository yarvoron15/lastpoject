from aiogram import types, Dispatcher
from config import bot
from buttons import inlinebuttons
from database import db


async def ask(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Type of food u prefer:",
        reply_markup=await inlinebuttons.question_for_food_type('Fruit', 'Vegetable', 'Cherry', 'Meat')
    )


async def answer_fruit(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich fruit do like most:",
        reply_markup=await inlinebuttons.type_fruit('Banana', 'Apple')
    )


async def answer_veg(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich vegetable do like most:",
        reply_markup=await inlinebuttons.type_vegetable('potato', 'tomato')
    )


async def answer_cherry(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich cherry do like most:",
        reply_markup=await inlinebuttons.type_cherry('red cherry', 'black cherry')
    )


async def answer_meat(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich meat do like most:",
        reply_markup=await inlinebuttons.type_meat('duck', 'sheep')
    )


async def yesno_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Have u ever eaten it?:",
        reply_markup=await inlinebuttons.yes_no("yes✅", "no❌")
    )


async def thanks(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Thank you for answering "
    )



async def answer_for_ban(call: types.CallbackQuery):
    datab = db.Database()
    count = datab.select_count_bun_table(tg_id=call.from_user.id)
    if count:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U r in the bad users list\n"
                 f"Amount of bad word: {count[0]}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Good for u\n"
                 "There is no ur name\n"
                 "Good boy"
        )





def register_ask(dp: Dispatcher):
    dp.register_callback_query_handler(ask, lambda call: call.data == "question")
    dp.register_callback_query_handler(answer_fruit, lambda call: call.data.startswith("aa"))
    dp.register_callback_query_handler(answer_veg, lambda call: call.data.startswith("cc"))
    dp.register_callback_query_handler(answer_cherry, lambda call: call.data.startswith("tt"))
    dp.register_callback_query_handler(answer_meat, lambda call: call.data.startswith("bb"))
    dp.register_callback_query_handler(yesno_answer, lambda call: call.data.startswith("pp"))
    dp.register_callback_query_handler(thanks, lambda call: call.data in ("yes",'no'))
    dp.register_callback_query_handler(answer_for_ban, lambda call: call.data == "bad")


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start_call,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        python_call,
        lambda call: call.data == "python"
    )
    dp.register_callback_query_handler(
        mojo_call,
        lambda call: call.data == "mojo"
    )
