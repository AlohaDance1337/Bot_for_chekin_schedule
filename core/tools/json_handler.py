import requests
from datetime import datetime
from core.tools import UniversalLogger

logger = UniversalLogger('http_request')


class JsonHandler:
    def __init__(self):
        self.url = "https://sevsu.samrzhevsky.ru/api/schedule?v=3.2&section=0&institute=4&group=ИКС%2Fб-21-1-о&week=8"
        self.numbering_of_classes = {
            1: '8:30',
            2: '10:10',
            3: '11:50',
            4: '14:00',
            5: '15:40',
            6: '17:20',
            7: '19:00',
        }

    def get_json(self):
        try:
            response = requests.get(self.url)
            today = datetime.now().strftime('%d.%m.%Y')
            if response.status_code == 200:
                data = response.json()
                days = data.get('schedule', [])

                # Фильтрация по завтрашней дате
                subjects = [day for day in days if day.get('date') == today]

                sub1 = [subject for subject in subjects if subject.get('subgroup') in ('1', '0')]
                sub2 = [subject for subject in subjects if subject.get('subgroup') in ('2', '0')]

                return sub1, sub2

            logger.error(f"Failed to fetch data, status code: {response.status_code}", extra='http_request')
            return [], []  # Возвращаем пустые списки в случае ошибки

        except Exception as e:
            logger.error(f"An error occurred: {e}", extra='http_request')
            return [], []  # Возвращаем пустые списки в случае ошибки

    def serialize_subjects(self, subjects):
        return [
            f'Время, пара, преподаватель, кабинет и тип пары: {self.numbering_of_classes.get(subject.get("n"))}, '
            f'{subject.get("lesson")}, {subject.get("teacher")}, {subject.get("location")}'
            for subject in subjects if subject.get("n") in self.numbering_of_classes
        ]

    def seralization_json(self):
        sub1, sub2 = self.get_json()
        str_for_sub1 = self.serialize_subjects(sub1)
        str_for_sub2 = self.serialize_subjects(sub2)

        return str_for_sub1, str_for_sub2
