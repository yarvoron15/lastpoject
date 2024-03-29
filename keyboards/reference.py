from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        "Link 🔗",
        callback_data="reference_link"
    )
    markup.add(reference_link_button)
    return markup