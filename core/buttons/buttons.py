from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def kb_schedule()-> ReplyKeyboardMarkup:
    button = ReplyKeyboardBuilder()
    button.button(text="Расписание")
    return button.as_markup(resize_keyboard = True)