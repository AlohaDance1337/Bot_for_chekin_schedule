from core.buttons import kb_schedule
from core.tools.json_handler import JsonHandler

from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
json_handler = JsonHandler()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer(
        text="Показывает расписание пар в универе. Для получения расписания ведите номер вашей подгруппы в виде цифры")


@router.message(F.text.in_(['1', '2']))
async def schadule(message: Message):
    response = int(message.text)
    subjects_for_first_subgroup, subjects_for_second_subgroup = json_handler.seralization_json()

    if response == 1:
        for subject in subjects_for_first_subgroup:
            await message.answer(text=subject)
    elif response == 2:
        for subject in subjects_for_second_subgroup:
            await message.answer(text=subject)
