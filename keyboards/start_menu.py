from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()

    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 🗒️",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 🔥",
        callback_data="registration"
    )
    random_profile_button = InlineKeyboardButton(
        "View Profiles 👍🏻👎🏻",
        callback_data="random_profile"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile 🐲",
        callback_data="my_profile"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(random_profile_button)
    markup.add(my_profile_button)
    return markup
