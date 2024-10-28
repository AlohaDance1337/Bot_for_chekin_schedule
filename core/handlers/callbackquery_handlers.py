from datetime import timedelta, datetime

from core.buttons import days_of_week

from aiogram.types import CallbackQuery
from aiogram import Router, F

from database import DatabaseHandler
from core.tools import JsonHandler

router = Router()
json_handler = JsonHandler()
db_handler = DatabaseHandler()





@router.callback_query(F.data.in_(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']))
async def get_schedule_for_day(call: CallbackQuery):
    data = call.data
    day_of_the_week = json_handler.get_next_weekday(data)
    user_group = db_handler.get_user(call.from_user.id)[2]
    subjects_for_first_subgroup, subjects_for_second_subgroup = await json_handler.seralization_json(day_of_the_week)
    if user_group == 1 and subjects_for_first_subgroup:
        subjects = subjects_for_first_subgroup
    elif user_group == 2 and subjects_for_second_subgroup:
        subjects = subjects_for_second_subgroup
    else:
        subjects = []


    if subjects:
        for subject in subjects:
            await call.message.answer(text=subject)
    else:
        await call.message.answer(text=f"Это {data.capitalize()}, можно кайфовать!")
from datetime import timedelta, datetime

from core.buttons import days_of_week

from aiogram.types import CallbackQuery
from aiogram import Router, F

from database import DatabaseHandler
from core.tools import JsonHandler

router = Router()
json_handler = JsonHandler()
db_handler = DatabaseHandler()





@router.callback_query(F.data.in_(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']))
async def get_schedule_for_day(call: CallbackQuery):
    data = call.data
    day_of_the_week = json_handler.get_next_weekday(data)
    user_group = db_handler.get_user(call.from_user.id)[2]
    subjects_for_first_subgroup, subjects_for_second_subgroup = await json_handler.seralization_json(day_of_the_week)
    if user_group == 1 and subjects_for_first_subgroup:
        subjects = subjects_for_first_subgroup
    elif user_group == 2 and subjects_for_second_subgroup:
        subjects = subjects_for_second_subgroup
    else:
        subjects = []


    if subjects:
        for subject in subjects:
            await call.message.answer(text=subject)
    else:
        await call.message.answer(text=f"Это {data.capitalize()}, можно кайфовать!")
from datetime import timedelta, datetime

from core.buttons import days_of_week

from aiogram.types import CallbackQuery
from aiogram import Router, F

from database import DatabaseHandler
from core.tools import JsonHandler

router = Router()
json_handler = JsonHandler()
db_handler = DatabaseHandler()


@router.callback_query(F.data.in_(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']))
async def get_schedule_for_day(call: CallbackQuery):
    data = call.data
    day_of_the_week = json_handler.get_next_weekday(data)
    user_group = db_handler.get_user(call.from_user.id)[2]
    subjects_for_first_subgroup, subjects_for_second_subgroup = await json_handler.seralization_json(day_of_the_week)
    if user_group == 1 and subjects_for_first_subgroup:
        subjects = subjects_for_first_subgroup
    elif user_group == 2 and subjects_for_second_subgroup:
        subjects = subjects_for_second_subgroup
    else:
        subjects = []

    if subjects:
        for subject in subjects:
            await call.message.answer(text=subject)
    else:
        await call.message.answer(text=f"Это {data.capitalize()}, можно кайфовать!")
