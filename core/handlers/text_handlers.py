from core.buttons import kb_schedule
from core.tools.json_handler import JsonHandler
from database import DatabaseHandler

from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
json_handler = JsonHandler()
db_handler = DatabaseHandler()

@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer(
        text="Показывает расписание пар в универе. Для получения расписания ведите номер вашей подгруппы в виде цифры, а потом нажмите на кнопку расписание", reply_markup = kb_schedule())

@router.message(F.text.in_(['1', '2']))
async def add_user_to_db(message:Message):
    db_handler.add_user(message.from_user.id,message.text)

@router.message(F.text=='Расписание')
async def schadule(message: Message):
    user_group = db_handler.get_user(message.from_user.id)[2]
    subjects_for_first_subgroup, subjects_for_second_subgroup = await json_handler.seralization_json()
    if subjects_for_first_subgroup and subjects_for_second_subgroup:  # Если хотя бы один список не пустой
        if user_group == 1 and subjects_for_first_subgroup:  # Проверяем только нужный список
            for subject in subjects_for_first_subgroup:
                await message.answer(text=subject)
        elif user_group == 2 and subjects_for_second_subgroup:
            for subject in subjects_for_second_subgroup:
                await message.answer(text=subject)
    else:
        await message.answer(text="Сегодня вторник, можно кайфовать")