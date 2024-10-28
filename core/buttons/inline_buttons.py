from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Расписание на день из недели', callback_data='schedule')]]
)

days_of_week = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Понедельник', callback_data='monday')],
    [InlineKeyboardButton(text='Вторник', callback_data='tuesday')],
    [InlineKeyboardButton(text='Среда', callback_data='wednesday')],
    [InlineKeyboardButton(text='Четверг', callback_data='thursday')],
    [InlineKeyboardButton(text='Пятница', callback_data='friday')],
    [InlineKeyboardButton(text='Суббота', callback_data='saturday')]]
    )

