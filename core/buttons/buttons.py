from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Универсальная функция для создания клавиатуры с одной кнопкой
def create_single_button_kb(button_text: str) -> ReplyKeyboardMarkup:
    button = ReplyKeyboardBuilder()
    button.button(text=button_text)
    return button.as_markup(resize_keyboard=True)


def kb_schedule() -> ReplyKeyboardMarkup:
    return create_single_button_kb("Расписание")


def kb_schedule_for_day() -> ReplyKeyboardMarkup:
    return create_single_button_kb("Расписание на день из недели")
