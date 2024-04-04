from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quest_button():
    markup = InlineKeyboardMarkup(row_width=1)
    v1 = InlineKeyboardButton('Quastions', callback_data='question')
    v2 = InlineKeyboardButton('Check for bad user', callback_data='bad')
    v3 = InlineKeyboardButton('Registration', callback_data='reg')
    v4 = InlineKeyboardButton('View profiles', callback_data='view')
    v5 = InlineKeyboardButton('Referral menu', callback_data='ferral')
    v6 = InlineKeyboardButton('news.kg', callback_data='scrap')
    markup.add(v1,v2,v3,v4,v5,v6)
    return markup

async def question_for_food_type(var1, var2, var3, var4):
    markup = InlineKeyboardMarkup(row_width=1)
    v1 = InlineKeyboardButton(var1, callback_data='aa'+var1)
    v2 = InlineKeyboardButton(var2, callback_data='cc'+var2)
    v3 = InlineKeyboardButton(var3, callback_data='tt'+var3)
    v4 = InlineKeyboardButton(var4, callback_data='bb'+var4)
    markup.add(v1, v2, v3, v4)
    return markup


async def type_fruit(var1, var2):
    markup = InlineKeyboardMarkup()
    v1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    v2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(v1, v2)
    return markup


async def type_vegetable(var1, var2):
    markup = InlineKeyboardMarkup()
    v1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    v2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(v1, v2)
    return markup


async def type_cherry(var1, var2):
    markup = InlineKeyboardMarkup()
    v1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    v2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(v1, v2)
    return markup


async def type_meat(var1, var2):
    markup = InlineKeyboardMarkup()
    v1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    v2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(v1, v2)
    return markup


async def yes_no(var1, var2):
    markup = InlineKeyboardMarkup()
    v1 = InlineKeyboardButton(var1, callback_data='yes')
    v2 = InlineKeyboardButton(var2, callback_data='no')
    markup.add(v1, v2)
    return markup

async def like_dislike(user):
    markup = InlineKeyboardMarkup(row_width=1)
    v1 = InlineKeyboardButton("Like👍", callback_data=f'Like_{user}')
    v2 = InlineKeyboardButton("Dislike👎", callback_data=f'Dislike_{user}')
    markup.add(v1, v2)
    return markup


async def generate_link():
    markup = InlineKeyboardMarkup(row_width=1)
    v1 = InlineKeyboardButton("Generate Link", callback_data='generate_link')
    v2 = InlineKeyboardButton("See referrals", callback_data='jjj')
    v3 = InlineKeyboardButton("Balance", callback_data='balance')
    markup.add(v1, v2, v3)
    return markup
