from aiogram import types, Dispatcher
from config import bot
from keyboards.questionnaire import questionnaire_keyboard


async def questionnaire_start_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python 🐍 or Mojo 🔥 ?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, im python developer too"
    )


async def mojo_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie Mojo still in alpha!"
    )


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
