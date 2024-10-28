import aiohttp
import asyncio
from datetime import datetime, timedelta
from core.tools import UniversalLogger

logger = UniversalLogger('http_request')


class JsonHandler:
    def __init__(self):
        self.base_url = "https://sevsu.samrzhevsky.ru/api/schedule?v=3.2&section=0&institute=4&group=ИКС%2Fб-21-1-о&week="
        self.numbering_of_classes = {
            1: '8:30',
            2: '10:10',
            3: '11:50',
            4: '14:00',
            5: '15:40',
            6: '17:20',
            7: '19:00',
        }

    @staticmethod
    def get_current_week() -> int:
        """Возвращает номер текущей недели, начиная с сентября."""
        start_of_september = datetime(datetime.now().year, 9, 1)
        current_week = (datetime.now() - start_of_september).days // 7 + 1
        return current_week

    @staticmethod
    def get_next_weekday(target_day):
        days_of_week = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
                        'friday': 4, 'saturday': 5, 'sunday': 6}

        today = datetime.now()
        today_weekday = today.weekday()  # Получаем текущий день недели (0=понедельник, 6=воскресенье)
        target_weekday = days_of_week[target_day.lower()]

        # Если целевой день уже прошел на этой неделе, прибавляем 7 дней
        days_until_next = (target_weekday - today_weekday + 7) % 7 or 7
        next_date = today + timedelta(days=days_until_next)

        return next_date.strftime('%d.%m.%Y')

    async def get_json(self , date):
        """Асинхронный метод для получения данных в формате JSON."""
        url = self.base_url + str(self.get_current_week())
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        days = data.get('schedule', [])

                        # Фильтрация по завтрашней дате
                        subjects = [day for day in days if day.get('date') == date]

                        sub1 = [subject for subject in subjects if subject.get('subgroup') in ('1', '0')]
                        sub2 = [subject for subject in subjects if subject.get('subgroup') in ('2', '0')]

                        return sub1, sub2

                    logger.error(f"Failed to fetch data, status code: {response.status}", extra='http_request')
                    return [], []  # Возвращаем пустые списки в случае ошибки

            except Exception as e:
                logger.error(f"An error occurred: {e}", extra='http_request')
                return [], []  # Возвращаем пустые списки в случае ошибки

    def serialize_subjects(self, subjects):
        return [
            f'Время, пара, преподаватель, кабинет и тип пары: {self.numbering_of_classes.get(subject.get("n"))},'
            f'{subject.get("lesson")}, {subject.get("teacher")}, {subject.get("location")}, {subject.get("type")}'
            for subject in subjects if subject.get("n") in self.numbering_of_classes
        ]

    async def seralization_json(self,date):
        """Асинхронный метод для сериализации данных."""
        sub1, sub2 = await self.get_json(date)
        str_for_sub1 = self.serialize_subjects(sub1)
        str_for_sub2 = self.serialize_subjects(sub2)

        return str_for_sub1, str_for_sub2
